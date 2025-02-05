import anthropic
import instructor

from pydantic import BaseModel, Field
from smolagents import Tool
from typing import Any, List, Optional
from loguru import logger
from enum import Enum

from src.client import DiffusionClient

MAX_IMAGES_PER_BATCH = 100

VISUAL_FEEDBACK_SYSTEM_PROMPT = """
You are an advanced video editing assistant that reviews a series of **image samples**, each taken **every 30 frames** from a video. The last sample is taken at the end of the video. The time is indicated in the upper right corner of each sample. Your job is to verify that the editing aligns with the given editing goal.

Your Task:
	•	Analyze each sample (not individual frames) to check if it meets the editing goal.
	•	If the sample meets the goal, respond with "Everything checks out."
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
    •	**Do NOT infer the exact video length** based on the number of samples. Use the time indicators seen in the samples instead.
	•	**Variations in shot composition** (e.g., wide shots vs. close-ups) are only problematic if they contradict the user's goal (e.g., if the goal specifies "consistent framing" but shots vary).
	•	**Only point out clear violations of the editing goal.** If you're not certain, explain exaclty why it's not aligned with the goal.
    •	**Be aware that the last frame might not have been sampled because it's not in the 30 frames range.**

Response Format:

✅ If the sample aligns with the editing goal:
	•	Approve the sample

❌ If there's an issue:
	•	"Issue detected: The text is not centered. Adjust the alignment to match the goal."
	•	"Issue detected: The animation is missing. Ensure the transition effect is applied as specified."
	•	"Issue detected: The clip is not trimmed correctly. Adjust the start and end points as required."

Be concise, clear, and actionable in your feedback. Avoid unnecessary details or subjective judgments.
"""


class IssueType(str, Enum):
    TEXT_POSITIONING = "text_positioning"
    ANIMATION = "animation"
    TRIMMING = "trimming"
    POSITIONING_SCALING = "positioning_scaling"
    VISUAL_ARTIFACT = "visual_artifact"

    @classmethod
    def from_description(cls, desc: str) -> "IssueType":
        if "text" in desc.lower() and (
            "center" in desc.lower() or "position" in desc.lower()
        ):
            return cls.TEXT_POSITIONING
        if "animation" in desc.lower():
            return cls.ANIMATION
        if "trim" in desc.lower():
            return cls.TRIMMING
        if "scale" in desc.lower() or "position" in desc.lower():
            return cls.POSITIONING_SCALING
        return cls.VISUAL_ARTIFACT


class IssueSeverity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class CompositionIssue(BaseModel):
    type: IssueType = Field(..., description="Type of issue detected")
    description: str = Field(..., description="Detailed description of the issue")
    frame_number: Optional[int] = Field(
        None, description="Frame number where issue occurs"
    )
    suggested_fix: str = Field(
        ..., description="Actionable suggestion to fix the issue"
    )

    def format_message(self) -> str:
        return f"Issue detected frame {self.frame_number}: {self.description}. {self.suggested_fix}"


class EditingGoalValidation(BaseModel):
    text_positioning_correct: bool = Field(
        ..., description="Text elements are properly centered/positioned"
    )
    animations_present: bool = Field(..., description="Required animations are present")
    trimming_correct: bool = Field(
        ..., description="Video trimming matches requirements"
    )
    elements_positioned: bool = Field(
        ..., description="All elements properly positioned and scaled"
    )
    no_artifacts: bool = Field(
        ..., description="No unintended visual artifacts present"
    )


class FrameAnalysis(BaseModel):
    frame_number: int = Field(..., description="Frame number being analyzed")
    issues: List[CompositionIssue] = Field(default_factory=list)
    is_ok: bool = Field(..., description="Whether frame meets requirements")

    def format_message(self) -> str:
        if self.is_ok:
            return "Everything checks out."
        return "\n".join(issue.format_message() for issue in self.issues)


class BatchAnalysis(BaseModel):
    frames: List[FrameAnalysis] = Field(default_factory=list)
    overall_decision: bool = Field(
        ..., description="Whether entire batch meets requirements"
    )

    @property
    def total_issues(self) -> int:
        return sum(len(frame.issues) for frame in self.frames)

    def format_message(self) -> str:
        if self.overall_decision:
            return "Everything checks out."
        messages = []
        for frame in self.frames:
            if not frame.is_ok:
                messages.extend(issue.format_message() for issue in frame.issues)
        return "\n".join(messages)


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

    def forward(
        self,
        final_goal: str = "The video should show a smooth transition between scenes without any glitches or artifacts.",
    ) -> Any:
        """Process video frames and get feedback."""
        samples = sorted(self.client.samples)

        logger.info(f"Processing {len(samples)} frames with goal: {final_goal}")

        prompt = f"Goal: **{final_goal}**"

        try:
            all_issues = []
            is_ok_overall = True
            total_frames = len(samples)
            batch_size = min(MAX_IMAGES_PER_BATCH, total_frames)

            for batch_start in range(0, total_frames, batch_size):
                batch = samples[batch_start : batch_start + batch_size]

                message_content = []
                for i, sample in enumerate(batch, 1):
                    current_frame = (
                        batch_start + i - 1
                    ) * 30  # Each sample is 30 frames apart
                    current_second = current_frame / 30  # Convert frames to seconds

                    print(f"Frame {current_frame} | Time: {current_second:.2f}s:")

                    message_content.extend(
                        [
                            {
                                "type": "text",
                                "text": f"Frame {current_frame} | Time: {current_second:.2f}s:",
                            },
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
                    system=VISUAL_FEEDBACK_SYSTEM_PROMPT,
                    messages=[{"role": "user", "content": message_content}],
                    response_model=BatchAnalysis,
                )

                logger.debug(f"Batch analysis: {batch_analysis}")

                if not batch_analysis.overall_decision:
                    all_issues.extend(
                        issue.format_message()
                        for frame in batch_analysis.frames
                        for issue in frame.issues
                    )
                is_ok_overall = is_ok_overall and batch_analysis.overall_decision

                logger.debug(f"is_ok_overall: {is_ok_overall}")

            return f"{'; '.join(all_issues)}; Render decision: {is_ok_overall}"

        except Exception as e:
            logger.error(f"Error processing frames: {str(e)}")
            return f"{str(e)}; Render decision: False"


if __name__ == "__main__":
    client = DiffusionClient()
    visual_feedback_tool = VisualFeedbackTool(client=client)

    # Step 1: Set up video and get samples
    logger.info("🎬 Setting up video...")

    # Upload assets first
    client.upload_assets(["assets/big_buck_bunny_1080p_30fps.mp4"])

    client.evaluate("""
    const videoFile = assets()[0];
    const video = new core.VideoClip(videoFile).subclip(0, 150);
    await composition.add(video);
    await sample();
    """)

    # Step 2: Run visual feedback analysis
    logger.info("🔍 Analyzing composition...")
    decision = visual_feedback_tool.forward(
        final_goal="""
        The video should have exactly 150 frames.
        """
    )

    logger.info(f"Analysis Results:\n{decision}")
