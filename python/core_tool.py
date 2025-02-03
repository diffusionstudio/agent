from utils import clear_file_path
from smolagents import Tool
from typing import Any
from loguru import logger
from diffusion_studio import DiffusionClient


class VideoEditorTool(Tool):
    name = "video_editor_tool"
    description = """A tool that connects to a remote browser and performs video editing operations using Diffusion Studio's web-based operator ui.
    Note: Documentation examples might be in TypeScript - remove type annotations before using, so that the code can be executed in a JavaScript environment.

    Common operations:
    - Clipping: `video.subclip(start_frame, end_frame)`
    - Offsetting: `video.offset(offset_frames)`
    - Trimming: `image.trim(start_frame, end_frame)`
    - Splitting: `await video.split(split_frames)`
    - Adding to timeline: `await composition.add(clip)`
    - Rendering: `await render()`
    """
    inputs = {
        "assets": {
            "type": "array",
            "description": "List of video assets to process. Default is the Big Buck Bunny sample, assets/big_buck_bunny_1080p_30fps.mp4",
            "nullable": False,
        },
        "js_code": {
            "type": "string",
            "description": "JavaScript code to execute in the editor.",
            "nullable": False,
        },
        "output": {
            "type": "string",
            "description": "Output path for the processed video. Default is output/video.mp4",
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
        const video = new core.VideoClip(videoFile);
        await composition.add(video);
        """,
        output: str = "output/video.mp4",
    ) -> Any:
        """Main execution method that processes the video editing task."""

        try:
            self.assets = assets
            self.output = output
            clear_file_path(output)
            logger.debug("State initialized")

            if self.client.page:
                self.input = self.client.page.locator("#file-input")
                logger.info("Received file input reference:", bool(self.input))
            else:
                raise Exception("Page not found")

            logger.info(f"Setting input file: {self.assets[0]}")
            self.input.set_input_files(self.assets[0])
            logger.debug("Input file set successfully")

            result = self.client.evaluate(js_code)
            logger.debug("Video editing task completed successfully")
            return result

        except Exception as e:
            logger.exception("Video editing task failed")
            raise e


if __name__ == "__main__":
    client = DiffusionClient()
    tool = VideoEditorTool(client=client)
    tool.forward()
