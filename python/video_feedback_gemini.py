import os
import time
from smolagents import Tool
from loguru import logger
from google.generativeai.client import configure
import google.generativeai as genai
from dotenv import load_dotenv
from typing import Any

load_dotenv()

# Configure API key
configure(api_key=os.getenv("GOOGLE_GEMINI_BASE_KEY"))


class VideoFeedbackGemini(Tool):
    name = "video_feedback"
    description = """Analyzes a video after editing to verify if it meets the user's goals using Gemini's video analysis capabilities."""

    inputs = {
        "video_path": {
            "type": "string",
            "description": "Path to the edited video file to analyze",
            "nullable": False,
            "required": True,
        },
        "final_goal": {
            "type": "string",
            "description": "What the user wanted to achieve with their video edits",
            "nullable": False,
            "required": True,
        },
    }
    output_type = "object"

    def __init__(self):
        super().__init__()
        self.model = genai.GenerativeModel(model_name="gemini-1.5-pro")

    def forward(
        self,
        video_path: str | None = "output/video.mp4",
        final_goal: str
        | None = "The video should show a smooth transition between scenes without any glitches or artifacts",
    ) -> Any:
        """Process video and get feedback"""
        if not video_path:
            video_path = "output/video.mp4"
        if not final_goal:
            final_goal = "The video should show a smooth transition between scenes without any glitches or artifacts"

        logger.info(f"Processing video: {video_path}")

        try:
            # Upload video
            logger.info("Uploading video...")
            video_file = genai.upload_file(path=video_path)
            logger.info(f"Completed upload: {video_file.uri}")

            # Wait for processing
            while video_file.state.name == "PROCESSING":
                logger.info("Waiting for video processing...")
                time.sleep(5)
                video_file = genai.get_file(video_file.name)

            if video_file.state.name == "FAILED":
                raise ValueError(f"Video processing failed: {video_file.state.name}")

            # Analyze video
            prompts = [
                f"""Analyze this video for the following goal: '{final_goal}'
                1. Describe any quality issues or artifacts
                2. Evaluate transitions between scenes
                3. Assess if the video meets the goal
                Be very concise - one short sentence per point.""",
                "Transcribe the audio and provide timestamps for key visual events.",
                "List any technical issues or areas that need improvement.",
            ]

            results = {}
            for prompt in prompts:
                response = self.model.generate_content(
                    [video_file, prompt], request_options={"timeout": 600}
                )
                results[prompt.split("\n")[0]] = response.text

            # Cleanup
            video_file.delete()

            return results

        except Exception as e:
            logger.error(f"Video analysis failed: {str(e)}")
            return {"error": str(e)}


def main():
    tool = VideoFeedbackGemini()
    results = tool.forward(
        video_path="python/output/video.mp4",
        final_goal="Analyze the video quality and transitions",
    )

    print("\nResults:")
    for prompt, result in results.items():
        print(f"\n=== {prompt} ===")
        print(result)
        print("=" * 50)


if __name__ == "__main__":
    main()
