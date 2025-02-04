import os
import tempfile
import anthropic
import instructor

from pydantic import BaseModel, Field
from smolagents import Tool
from diffusion_studio import DiffusionClient
from typing import Any, List, Optional
from loguru import logger
from core_tool import VideoEditorTool

MAX_IMAGES_PER_BATCH = 100

class RenderDecision(BaseModel):
    is_ok_overall: bool = Field(
        ..., description="Whether the frames match the user requirements"
    )


class FrameAnalysis(BaseModel):
    composition_issues: Optional[List[str]] = Field(
        default_factory=list, description="List of detected composition issues if any"
    )
    render_decision: RenderDecision = Field(
        ..., description="Render decision based on overall composition quality"
    )


class VisualFeedbackTool(Tool):
    name = "visual_feedback"
    description = """
    Analyzes video composition quality and makes render decisions taking into account the composition goal.
    Works in conjunction with VideoEditorTool to validate edits before rendering.
    """

    inputs = {
        "final_goal": {
            "type": "string",
            "description": "Quality criteria to evaluate (e.g. 'Ensure smooth transitions', 'Check for visual artifacts')",
            "nullable": False,
            "required": True,
        },
    }
    output_type = "object"

    def __init__(self, client: DiffusionClient):
        super().__init__()
        # Use sync client
        base_client = anthropic.Anthropic()
        self.anthropic_client = instructor.from_anthropic(base_client)
        self.model = "claude-3-5-sonnet-latest"
        self.client = client
        self.temp_dir = tempfile.mkdtemp()

    def forward(
        self,
        final_goal: str = "The video should show a smooth transition between scenes without any glitches or artifacts.",
    ) -> Any:
        """Process video frames and get feedback."""
        samples = sorted(self.client.samples)

        logger.info(f"Processing {len(samples)} frames with goal: {final_goal}")

        prompt = f"""Analyze these frames for composition quality:
        User composition goal: {final_goal}
        """

        try:
            all_issues = []
            is_ok_overall = True
            total_frames = len(samples)
            batch_size = min(MAX_IMAGES_PER_BATCH, total_frames)

            for batch_start in range(0, total_frames, batch_size):
                batch = samples[batch_start : batch_start + batch_size]

                message_content = []
                for i, sample in enumerate(batch, 1):
                    message_content.extend(
                        [
                            {"type": "text", "text": f"Frame {batch_start + i}:"},
                            {
                                "type": "image",
                                "source": {
                                    "type": "base64",
                                    "media_type": "image/jpeg",
                                    "data": sample,
                                },
                            },
                        ]
                    )

                message_content.append({"type": "text", "text": prompt})
                logger.info(f"Processing batch of {len(batch)} frames")

                batch_analysis = self.anthropic_client.messages.create(
                    model=self.model,
                    max_tokens=1024,
                    messages=[{"role": "user", "content": message_content}],
                    response_model=FrameAnalysis,
                )

                logger.debug(f"Batch analysis: {batch_analysis}")

                if batch_analysis.composition_issues:
                    all_issues.extend(batch_analysis.composition_issues)
                is_ok_overall = (
                    is_ok_overall and batch_analysis.render_decision.is_ok_overall
                )

                logger.debug(f"is_ok_overall: {is_ok_overall}")

                # Cleanup batch frames
                for frame_name in batch:
                    frame_path = os.path.join("samples", frame_name)
                    try:
                        logger.debug(f"Deleting frame {frame_path}")
                        os.remove(frame_path)
                    except Exception as e:
                        logger.warning(f"Failed to delete frame {frame_path}: {e}")

            return FrameAnalysis(
                composition_issues=all_issues,
                render_decision=RenderDecision(is_ok_overall=is_ok_overall),
            )

        except Exception as e:
            logger.error(f"Error processing frames: {str(e)}")
            return FrameAnalysis(
                composition_issues=[str(e)],
                render_decision=RenderDecision(is_ok_overall=False),
            )


# if __name__ == "__main__":
#     client = DiffusionClient()

#     core_tool = VideoEditorTool(client=client)
#     visual_feedback_tool = VisualFeedbackTool(client=client)

#     # Step 1: Composition
#     logger.info("🎬  Composing video...")
#     core_tool.forward(
#         assets=["assets/big_buck_bunny_1080p_30fps.mp4"],
#         js_code="""
#         // Create a 150 frames subclip
#         const videoFile = assets()[0];
#         const video = new core.VideoClip(videoFile).subclip(0, 150);
#         await composition.add(video);
#         """,
#         ready_to_render=False,  # Initial composition, will auto-append sample()
#     )

#     # Step 2: Analysis
#     logger.info("🔍 Analyzing composition...")
#     decision = visual_feedback_tool.forward(
#         final_goal="""Analyze the video composition focusing on:
#         1. Overall flow and pacing between scenes
#         2. Visual consistency and quality
#         3. Transition opportunities and potential issues

#         Minor imperfections are acceptable if they don't impact the viewing experience.
#         Focus on issues that would be noticeable to the average viewer."""
#     )

#     logger.info(f"Decision: {decision}")
