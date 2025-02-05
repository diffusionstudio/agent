import tempfile
import anthropic
import instructor

from pydantic import BaseModel, Field
from smolagents import Tool
from client import DiffusionClient
from typing import Any, List, Optional
from loguru import logger

MAX_IMAGES_PER_BATCH = 100

VISUAL_FEEDBACK_PROMPT = """
You are an advanced video editing assistant that reviews a series of **image samples**, each taken **every 30 frames** from a video. The time is indicated in the upper right corner of each sample. Your job is to verify that the editing aligns with the given editing goal.

Your Task:
	•	Analyze each sample (not individual frames) to check if it meets the editing goal.
	•	If the sample meets the goal, respond with “Everything checks out.”
	•	If the sample reveals an issue, provide clear and actionable feedback.

Editing Mistakes to Detect:
	1.	Editing Goal Compliance:
	•	Text Positioning: Text should be centered but isn't.
	•	Missing Animation: An expected effect is absent.
	•	Trimming Issues: The clip wasn't trimmed correctly based on the goal.
	•	Positioning & Scaling Errors: Elements (video, text, graphics) aren't placed properly in the composition.
	2.	Common-Sense Issues (Even Without Explicit User Instruction):
	•	If a clip should be trimmed, but the subject is not centered or properly scaled in the composition.
	•	Visual artifacts or unnatural elements that would not appear in a polished video.

Important Clarifications:
    •	**Do NOT mistake a sample for frames or seconds.** You are analyzing images taken every 30 frames or 1 second, not continuous frames.
	•	**Do NOT judge video quality** (e.g., resolution, lighting, camera work) unless the issue affects editing alignment.
	•	**Do NOT assume a video is too long or too short based on sample similarity.** Instead, verify if the actual length aligns with the edit goal.
	•	**Variations in shot composition** (e.g., wide shots vs. close-ups) are only problematic if they contradict the user's goal (e.g., if the goal specifies “consistent framing” but shots vary).
	•	**Only point out clear violations of the editing goal.** If you're not certain, explain exaclty why it's not aligned with the goal.
    •	**Be aware that the last frame might not have been sampled because it's not in the 30 frames range.** 
    •	**Do NOT infer the exact video length** based on the number of samples. Use the time indicators seen in the samples instead.

Response Format:

✅ If the sample aligns with the editing goal:
	•	"Everything checks out."

❌ If there's an issue:
	•	"Issue detected: The text is not centered. Adjust the alignment to match the goal."
	•	"Issue detected: The animation is missing. Ensure the transition effect is applied as specified."
	•	"Issue detected: The clip is not trimmed correctly. Adjust the start and end points as required."

Be concise, clear, and actionable in your feedback. Avoid unnecessary details or subjective judgments.
"""


class FrameAnalysis(BaseModel):
    composition_issues: Optional[List[str]] = Field(
        default_factory=list, description="List of detected composition issues if any"
    )
    render_decision: bool = Field(
        ..., description="Whether the frames match the user requirements"
    )


class VisualFeedbackTool(Tool):
    name = "visual_feedback"
    description = """
    Analyzes video composition quality and makes render decisions taking into account the composition goal.
    Works in conjunction with VideoEditorTool to validate edits before rendering. Can point out issues with the video composition,
    which need to be fixed before rendering by the VideoEditorTool.
    """

    inputs = {
        "final_goal": {
            "type": "string",
            "description": "Quality criteria to evaluate (e.g. 'Ensure clip position are correct', 'Check for visual artifacts')",
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

        prompt = f"{VISUAL_FEEDBACK_PROMPT}\n\nGoal: **{final_goal}**"

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
                            {"type": "text", "text": f"Sample {batch_start + i}:"},
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
                is_ok_overall = is_ok_overall and batch_analysis.render_decision

                logger.debug(f"is_ok_overall: {is_ok_overall}")

            return f'{all_issues}; Render decision: {is_ok_overall}'

        except Exception as e:
            logger.error(f"Error processing frames: {str(e)}")
            return f'{str(e)}; Render decision: False'


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
