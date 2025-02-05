from smolagents import Tool
from typing import Any
from loguru import logger
from client import DiffusionClient


class VideoEditorTool(Tool):
    name = "video_editor_tool"
    description = """A tool that performs video editing operations using Diffusion Studio's web-based editor.
    Handles both composition and rendering operations based on ready_to_render flag.
    If ready_to_render=False, will automatically append sample() for analysis.
    If ready_to_render=True, will ensure render() is present.

    The tool is designed to be used in conjunction with the VisualFeedbackTool.
    The VisualFeedbackTool will make a render decision based on the overall composition quality.
    The VideoEditorTool will then use the render decision to determine if the composition is ready to render.

    Common operations:
    - Clipping: `video.subclip(start_frame, end_frame)`
    - Offsetting: `video.offset(offset_frames)`
    - Trimming: `image.trim(start_frame, end_frame)`
    - Splitting: `await video.split(split_frames)`

    - Adding to timeline: `await composition.add(clip)`
    - Sampling: `await sample()`
    - Rendering: `await render()` // when composition is ready to be rendered
    """
    inputs = {
        "assets": {
            "type": "array",
            "description": "List of video assets to process",
            "nullable": False,
        },
        "js_code": {
            "type": "string",
            "description": "JavaScript code for video operations. render()/sample() will be auto-managed based on ready_to_render flag",
            "nullable": False,
        },
        "output": {
            "type": "string",
            "description": "Output path for the processed video (only used when rendering)",
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
        js_code: str = """
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

        return self.client.evaluate(js_code)

# if __name__ == "__main__":
#     client = DiffusionClient()
#     tool = VideoEditorTool(client=client)
#     tool.forward()
