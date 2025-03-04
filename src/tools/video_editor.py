from smolagents import Tool
from typing import Any
from loguru import logger

from src.client import DiffusionClient

class VideoEditorTool(Tool):
    name = "video_editor_tool"
    description = """A tool that performs video editing operations using Diffusion Studio's web-based editor.

    The tool is designed to be used in conjunction with the VisualFeedbackTool.
    The VisualFeedbackTool will verify if the composition can be rendered based on the overall composition quality.
    The VideoEditorTool can then call `await render()` if user has requested to render the video.

    Common operations:
    - Clipping: `video.subclip(start_frame, end_frame)`
    - Offsetting: `video.offset(offset_frames)`
    - Trimming: `image.trim(start_frame, end_frame)`
    - Splitting: `await video.split(split_frames)`
    - Adding to timeline: `await composition.add(clip)`
    - Sampling: `await sample()`
    """
    inputs = {
        "assets": {
            "type": "array",
            "description": "List of video assets to process",
            "nullable": False,
        },
        "javascript": {
            "type": "string",
            "description": "JavaScript code to manipulate the current composition",
            "nullable": False,
        },
        "output": {
            "type": "string",
            "description": "Output path for the processed video (only used when rendering). Use output/video.mp4 by default.",
            "nullable": False,
        },
    }
    output_type = "string"

    def __init__(self, client: DiffusionClient):
        """Initialize the tool with empty state. State is populated in forward()."""
        super().__init__()
        self.client: DiffusionClient = client
        logger.debug("DiffusionClient initialized")

    def forward(
        self,
        assets: list[str] = ["assets/big_buck_bunny_1080p_30fps.mp4"],
        javascript: str = """
        // Default example: Create a 150 frames subclip
        const videoFile = assets()[0];
        const video = new core.VideoClip(videoFile).subclip(0, 150);
        await composition.add(video);
        """,
        output: str = "output/video.mp4",
    ) -> Any:
        """Main execution method that processes the video editing task."""

        # Set output path and clear existing file (done by setter)
        self.client.output = output
        self.client.upload_assets(assets)

        return self.client.evaluate(javascript)

# if __name__ == "__main__":
#     client = DiffusionClient()
#     tool = VideoEditorTool(client=client)
#     tool.forward()
