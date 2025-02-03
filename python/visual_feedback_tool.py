import os
import tempfile
import base64
import anthropic
import asyncio
from tqdm import tqdm
import threading

from smolagents import Tool
from diffusion_studio import DiffusionClient
from typing import Dict, Any, List
from loguru import logger
from core_tool import VideoEditorTool


class ClaudeAnalysis:
    def __init__(self):
        self.anthropic_client = anthropic.AsyncAnthropic()
        self.model = "claude-3-5-sonnet-latest"

    async def analyze_image_async(self, image_path: str, prompt: str) -> str:
        """Analyze image using Claude Vision asynchronously"""
        try:
            with open(image_path, "rb") as f:
                image_data = base64.b64encode(f.read()).decode()

            # Get media type from file extension
            media_type = "image/jpeg" if image_path.endswith(".jpg") else "image/png"

            message = await self.anthropic_client.messages.create(
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

    def analyze_images_batch(
        self, image_paths: List[str], prompts: List[str]
    ) -> List[str]:
        """Analyze multiple images concurrently in a separate thread"""
        results_container = []  # Container to store results from the thread

        def run_async_in_thread():
            async def process_all():
                tasks = []
                for img_path, prompt in zip(image_paths, prompts):
                    # Fix path to include samples directory
                    full_path = os.path.join("samples", img_path)
                    task = self.analyze_image_async(full_path, prompt)
                    tasks.append(task)

                results = []
                for task in tqdm(
                    asyncio.as_completed(tasks),
                    total=len(tasks),
                    desc="Analyzing frames",
                ):
                    result = await task
                    results.append(result)
                return results

            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            try:
                results = loop.run_until_complete(process_all())
                results_container.extend(results)  # Store results in the container
            finally:
                loop.close()

        # Run async code in a separate thread
        thread = threading.Thread(target=run_async_in_thread)
        thread.start()
        thread.join()

        return results_container  # Return the results from the container

    def _process_frames(
        self, frame_paths: List[str], final_goal: str
    ) -> Dict[str, Dict[str, str]]:
        """Process all frames with progress tracking"""
        prompt = f"""You are a professional video editor. Analyze this frame for editing goal: '{final_goal}'
Focus ONLY on editing and composition quality, not scene content.
Keep each answer to 10-15 words maximum:

1. Composition quality (framing, balance, visual flow)
2. Technical issues (artifacts, glitches, quality loss)
3. Transition potential (how well it would cut/transition)"""

        try:
            # Create prompts list
            prompts = [prompt] * len(frame_paths)

            # Process frames in batch with progress bar
            analyses = self.analyze_images_batch(frame_paths, prompts)

            # Format results
            results = {}
            for i, (frame_name, analysis) in enumerate(zip(frame_paths, analyses), 1):
                frame_path = os.path.join("samples", frame_name)

                # Format points consistently
                lines = []
                points = ["1.", "2.", "3."]
                for line in analysis.split("\n"):
                    line = line.strip()
                    if not line:
                        continue
                    for p in points:
                        if p in line:
                            line = line[line.find(p) + len(p) :].strip()
                    lines.append(line)

                formatted_lines = [f"{j}. {line}" for j, line in enumerate(lines, 1)]

                results[f"frame_{i}"] = {
                    "frame_path": frame_path,
                    "analysis": "\n".join(formatted_lines),
                }

                # Delete frame after analysis
                try:
                    os.remove(frame_path)
                    logger.debug(f"Deleted frame: {frame_path}")
                except Exception as e:
                    logger.warning(f"Failed to delete frame {frame_path}: {e}")

            return results
        except Exception as e:
            logger.error(f"Error processing frames: {str(e)}")
            return {"error": {"frame_path": "", "analysis": f"Error: {str(e)}"}}


class VisualFeedbackTool(Tool):
    name = "visual_feedback"
    description = """Analyzes a video after editing to verify if it meets the user's goals.
    This tool is designed to be used after VideoEditorTool to validate if the edits achieved the desired outcome.
    It extracts frames at regular intervals and uses Claude Vision to check for quality, consistency, and goal achievement."""

    inputs = {
        "final_goal": {
            "type": "string",
            "description": "What the user wanted to achieve with their video edits (e.g., 'Remove all text overlays', 'Speed up slow sections')",
            "nullable": False,
            "required": True,
        },
    }
    output_type = "object"

    def __init__(self, client: DiffusionClient):
        super().__init__()
        self.claude = ClaudeAnalysis()
        self.client = client
        self.temp_dir = tempfile.mkdtemp()

    def _extract_frames(self) -> List[str]:
        """Get frames from samples directory"""
        samples_dir = "./samples"
        if not os.path.exists(samples_dir):
            raise ValueError(f"Samples directory not found: {samples_dir}")

        frame_paths = [
            os.path.join(samples_dir, f)
            for f in os.listdir(samples_dir)
            if f.startswith("sample-") and f.endswith(".png")
        ]
        frame_paths.sort()  # Ensure order

        if not frame_paths:
            raise ValueError("No sample frames found")

        return frame_paths

    def _process_frames(
        self, frame_paths: List[str], final_goal: str
    ) -> Dict[str, Dict[str, str]]:
        """Process all frames with progress tracking"""
        prompt = f"""You are a professional video editor. Analyze this frame for editing goal: '{final_goal}'
        Focus ONLY on editing and composition quality, not scene content.
        Keep each answer to 10-15 words maximum:

        1. Composition quality (framing, balance, visual flow)
        2. Technical issues (artifacts, glitches, quality loss)
        3. Transition potential (how well it would cut/transition)
        """

        try:
            # Create prompts list
            prompts = [prompt] * len(frame_paths)

            # Process frames in batch with progress bar
            analyses = self.claude.analyze_images_batch(frame_paths, prompts)

            # Format results
            results = {}
            for i, (frame_name, analysis) in enumerate(zip(frame_paths, analyses), 1):
                frame_path = os.path.join("samples", frame_name)

                # Format points consistently
                lines = []
                points = ["1.", "2.", "3."]
                for line in analysis.split("\n"):
                    line = line.strip()
                    if not line:
                        continue
                    for p in points:
                        if p in line:
                            line = line[line.find(p) + len(p) :].strip()
                    lines.append(line)

                formatted_lines = [f"{j}. {line}" for j, line in enumerate(lines, 1)]

                results[f"frame_{i}"] = {
                    "frame_path": frame_path,
                    "analysis": "\n".join(formatted_lines),
                }

                # Delete frame after analysis
                try:
                    os.remove(frame_path)
                    logger.debug(f"Deleted frame: {frame_path}")
                except Exception as e:
                    logger.warning(f"Failed to delete frame {frame_path}: {e}")

            return results
        except Exception as e:
            logger.error(f"Error processing frames: {str(e)}")
            return {"error": {"frame_path": "", "analysis": f"Error: {str(e)}"}}

    def forward(
        self,
        final_goal: str = "The video should show a smooth transition between scenes without any glitches or artifacts.",
    ) -> Any:
        """Process video frames and get feedback."""
        try:
            # Generate sample frames
            self.client.evaluate("await sample()")
            logger.info("Generated sample frame")

            # Get list of frames
            frames = sorted(
                [f for f in os.listdir("samples") if f.startswith("sample-")]
            )
            logger.info(f"Found {len(frames)} frames to analyze")

            # Process frames synchronously
            results = self._process_frames(frames, final_goal)
            return results

        except Exception as e:
            logger.error("Video analysis failed")
            raise e

    def __del__(self):
        """Cleanup temp files"""
        import shutil

        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)


def main():
    client = DiffusionClient()
    core_tool = VideoEditorTool(client=client)
    tool = VisualFeedbackTool(client=client)

    core_tool.forward(
        assets=["assets/big_buck_bunny_1080p_30fps.mp4"],
        js_code="""
        // Default example: Create a 150 frames subclip
        const videoFile = assets()[0];
        const video = new core.VideoClip(videoFile).subclip(0, 150);
        await composition.add(video);
        """,
    )

    results = tool.forward(
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
