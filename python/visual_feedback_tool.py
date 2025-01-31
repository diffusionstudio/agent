import cv2
import os
import tempfile
import base64
import asyncio
from smolagents import Tool
from typing import Dict, Any, List, Union
from loguru import logger
import anthropic


class ClaudeVisionTool:
    def __init__(self):
        self.client = anthropic.AsyncAnthropic()
        self.model = "claude-3-5-sonnet-latest"

    async def analyze_image(self, image_path: str, prompt: str) -> str:
        """Analyze image using Claude Vision"""
        try:
            with open(image_path, "rb") as f:
                image_data = base64.b64encode(f.read()).decode()

            # Get media type from file extension
            media_type = "image/jpeg" if image_path.endswith(".jpg") else "image/png"

            message = await self.client.messages.create(
                model=self.model,
                max_tokens=4096,
                temperature=0.5,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "image",
                                "source": {
                                    "type": "base64",
                                    "media_type": media_type,
                                    "data": image_data,
                                },
                            },
                            {
                                "type": "text",
                                "text": prompt
                                + "\nBe very concise - one short sentence per point.",
                            },
                        ],
                    }
                ],
            )

            # Extract text content from message
            content = str(message.content[0])
            if "TextBlock" in content:
                import re

                match = re.search(r"text=['\"]([^'\"]*)['\"]", content)
                if match:
                    return match.group(1).strip()
            return content.strip()
        except Exception as e:
            logger.error(f"Error analyzing image {image_path}: {str(e)}")
            return "Error analyzing frame"

    async def analyze_images_batch(
        self, image_paths: List[str], prompts: List[str]
    ) -> List[str]:
        """Analyze multiple images in parallel"""
        tasks = [
            self.analyze_image(img_path, prompt)
            for img_path, prompt in zip(image_paths, prompts)
        ]
        return await asyncio.gather(*tasks)


class VisualFeedbackTool(Tool):
    name = "visual_feedback"
    description = """Analyzes a video after editing to verify if it meets the user's goals.
    This tool is designed to be used after VideoEditorTool to validate if the edits achieved the desired outcome.
    It extracts frames at regular intervals and uses Claude Vision to check for quality, consistency, and goal achievement."""

    inputs = {
        "video_path": {
            "type": "string",
            "description": "Path to the edited video file to analyze (output from VideoEditorTool)",
            "nullable": False,
            "required": True,
        },
        "interval_seconds": {
            "type": "string",
            "description": "Interval in seconds between frame captures. Recommended: 1s for short videos (<30s), 2s for medium (30-120s), 5s for long (>120s)",
            "nullable": False,
            "required": True,
            "default": "5.0",  # Conservative default
        },
        "final_goal": {
            "type": "string",
            "description": "What the user wanted to achieve with their video edits (e.g., 'Remove all text overlays', 'Speed up slow sections')",
            "nullable": False,
            "required": True,
        },
    }
    output_type = "object"

    def __init__(self):
        super().__init__()
        self.claude = ClaudeVisionTool()
        self.temp_dir = tempfile.mkdtemp()

    def _extract_frames(self, video_path: str, interval_seconds: float) -> List[str]:
        """Extract frames from video at specified intervals"""
        if not os.path.exists(video_path):
            raise ValueError(f"Video file not found: {video_path}")

        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            raise ValueError(f"Could not open video: {video_path}")

        # Get video duration and validate interval
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        duration_seconds = total_frames / fps

        # Adjust interval if it would produce too many frames
        max_frames = 50  # Reasonable limit for API calls
        if (duration_seconds / interval_seconds) > max_frames:
            suggested_interval = duration_seconds / max_frames
            logger.warning(
                f"Interval {interval_seconds}s would produce too many frames. Using {suggested_interval:.1f}s instead"
            )
            interval_seconds = suggested_interval

        frame_interval = int(fps * interval_seconds)
        frame_paths = []
        frame_count = 0

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            if frame_count % frame_interval == 0:
                frame_path = os.path.join(self.temp_dir, f"frame_{frame_count}.jpg")
                cv2.imwrite(frame_path, frame)
                frame_paths.append(frame_path)

            frame_count += 1

        cap.release()
        return frame_paths

    async def _process_frames(
        self, frame_paths: List[str], interval_seconds: float, final_goal: str
    ) -> Dict[str, Dict[str, str]]:
        """Process all frames in parallel"""
        prompts = [
            f"""Analyze this frame for goal: '{final_goal}'
Keep each answer to 10-15 words maximum:

1. What's in the frame?
2. Any quality issues?
3. Good for transitions?"""
            for _ in frame_paths
        ]

        try:
            analyses = await self.claude.analyze_images_batch(frame_paths, prompts)

            # Clean up and format responses
            results = {}
            for i, (frame_path, analysis) in enumerate(zip(frame_paths, analyses)):
                timestamp = f"{i * interval_seconds:.1f}s"
                clean_analysis = analysis.replace("\\n", "\n").strip()

                # Format points consistently
                lines = []
                points = ["1.", "2.", "3."]
                for line in clean_analysis.split("\n"):
                    line = line.strip()
                    if not line:
                        continue
                    # Remove any existing numbers
                    for p in points:
                        if p in line:
                            line = line[line.find(p) + len(p) :].strip()
                    lines.append(line)

                # Add correct numbering
                formatted_lines = []
                for j, line in enumerate(lines, 1):
                    formatted_lines.append(f"{j}. {line}")

                results[timestamp] = {
                    "frame_path": frame_path,
                    "analysis": "\n".join(formatted_lines),
                }

            return results
        except Exception as e:
            logger.error(f"Error processing frames: {str(e)}")
            return {"error": {"frame_path": "", "analysis": f"Error: {str(e)}"}}

    def forward(
        self,
        video_path: str | None = "output/video.mp4",
        interval_seconds: Union[
            str, float, None
        ] = "1.0",  # Changed default to 1s for short videos
        final_goal: str
        | None = "The video should show a smooth transition between scenes without any glitches or artifacts",
    ) -> Any:
        """Process video and get feedback for frames"""
        if not video_path:
            video_path = "output/video.mp4"
        if not interval_seconds:
            interval_seconds = "5.0"
        if not final_goal:
            final_goal = "The video should show a smooth transition between scenes without any glitches or artifacts"

        # Convert interval_seconds to float
        interval_float = float(interval_seconds)

        logger.info(f"Processing video: {video_path}")
        logger.info(f"Extracting frames every {interval_float} seconds")
        logger.info(f"Final goal: {final_goal}")

        frame_paths = self._extract_frames(video_path, interval_float)

        # Create event loop and run async processing
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            results = loop.run_until_complete(
                self._process_frames(frame_paths, interval_float, final_goal)
            )
            logger.info("Completed video analysis")
            return results
        finally:
            loop.close()

    def __del__(self):
        """Cleanup temp files"""
        import shutil

        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)


def main():
    tool = VisualFeedbackTool()
    results = tool.forward(
        video_path="python/output/video.mp4",
        interval_seconds="5.0",  # Now passing as string
        final_goal="The video should show a smooth transition between scenes without any glitches or artifacts",
    )

    # Print results in a readable format
    for timestamp, data in results.items():
        print(f"\n=== Frame at {timestamp} ===")
        print(f"Frame path: {data['frame_path']}")
        print(f"Analysis: {data['analysis']}")
        print("=" * 50)


if __name__ == "__main__":
    main()
