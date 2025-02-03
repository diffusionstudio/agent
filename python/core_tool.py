from utils import clear_file_path
from smolagents import Tool
from typing import Any
from loguru import logger
from diffusion_studio import DiffusionClient
import asyncio


class VideoEditorTool(Tool):
    name = "video_editor_tool"
    description = """A tool that performs video editing operations using Diffusion Studio's web-based editor.
    Handles both composition and rendering operations based on ready_to_render flag.
    If ready_to_render=False, will automatically append sample() for analysis.
    If ready_to_render=True, will ensure render() is present.

    Common operations:
    - Clipping: `video.subclip(start_frame, end_frame)`
    - Offsetting: `video.offset(offset_frames)`
    - Trimming: `image.trim(start_frame, end_frame)`
    - Splitting: `await video.split(split_frames)`
    - Adding to timeline: `await composition.add(clip)`
    - Rendering: `await render()` (requires ready_to_render=True)
    - Sampling: `await sample()` (auto-added when ready_to_render=False)
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
        "ready_to_render": {
            "type": "boolean",
            "description": "Controls whether to render (True) or sample for analysis (False). Will strip render() if False, ensure render() if True",
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
        ready_to_render: bool = False,
    ) -> Any:
        """Main execution method that processes the video editing task."""
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            # If no loop is running, create a new one
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            try:
                return loop.run_until_complete(
                    self._async_forward(assets, js_code, output, ready_to_render)
                )
            finally:
                loop.close()
        else:
            # If we're already in an event loop, just create the coroutine
            return loop.create_task(
                self._async_forward(assets, js_code, output, ready_to_render)
            )

    async def _async_forward(
        self,
        assets: list[str],
        js_code: str,
        output: str,
        ready_to_render: bool,
    ) -> str:
        """Async implementation of the forward method."""
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
            await self.input.set_input_files(self.assets[0])
            logger.debug("Input file set successfully")

            if not ready_to_render and "render()" in js_code:
                js_code = js_code.replace("await render();", "")
                js_code = js_code.replace("// Render final video\n", "")

            # Get the indentation of the last line
            last_line = js_code.strip().split("\n")[-1]
            indentation = " " * (len(last_line) - len(last_line.lstrip()))

            if ready_to_render and "render()" not in js_code:
                js_code += f"\n{indentation}// Render final video\n{indentation}await render();"
            elif not ready_to_render and "sample()" not in js_code:
                js_code += f"\n{indentation}// Generate samples for analysis\n{indentation}await sample();"

            result = await self.client.evaluate(js_code)
            logger.debug("Video editing task completed successfully")
            return result

        except Exception as e:
            logger.exception("Video editing task failed")
            raise e


if __name__ == "__main__":

    async def test():
        client = DiffusionClient()
        await client.init()
        try:
            tool = VideoEditorTool(client=client)
            await tool.forward()
        finally:
            await client.close()

    asyncio.run(test())
