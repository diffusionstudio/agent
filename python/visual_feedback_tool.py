import os
import time
from smolagents import Tool
from typing import Any, Optional
from loguru import logger
from google.generativeai.client import configure
from google.generativeai.generative_models import GenerativeModel
from google.generativeai.files import upload_file, get_file
from google.generativeai.types import GenerationConfig

# Configure API key
configure(api_key=os.getenv("GOOGLE_API_KEY"))


class VisualFeedbackTool(Tool):
    name = "visual_feedback"
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
        self.model = GenerativeModel("gemini-1.5-pro")

    def forward(
        self,
        video_path: Optional[str] = "output/video.mp4",
        final_goal: Optional[
            str
        ] = "The video should show a smooth transition between scenes without any glitches or artifacts",
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
            video_file = upload_file(video_path)
            logger.info(f"Completed upload: {video_file.uri}")

            # Wait for processing
            while video_file.state == "PROCESSING":
                logger.info("Waiting for video processing...")
                time.sleep(5)
                video_file = get_file(video_file.name)

            if video_file.state == "FAILED":
                raise ValueError(f"Video processing failed: {video_file.state}")

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
                    [video_file, prompt],
                    generation_config=GenerationConfig(temperature=0.4),
                )
                results[prompt.split("\n")[0]] = response.text

            # Cleanup
            video_file.delete()

            return results

        except Exception as e:
            logger.error(f"Video analysis failed: {str(e)}")
            return {"error": str(e)}
