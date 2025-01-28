from playwright.async_api import async_playwright, Playwright, Page, Browser
from utils import clear_file_path
from smolagents import Tool
from typing import Optional, Any
import asyncio
from loguru import logger
import os


class VideoEditorTool(Tool):
    name = "video_editor_tool"
    description = """A tool that connects to a remote browser and performs video editing operations using DiffStudio's web-based editor.
    Note: Documentation examples are in TypeScript - remove type annotations before using.

    Common operations:
    - Clipping: video.subclip(start_frame, end_frame)
    - Offsetting: video.offset(offset_frames)
    - Trimming: image.trim(start_frame, end_frame)
    - Splitting: video.split(split_frames)
    - Adding to timeline: composition.add(clip)
    - Rendering: await render()

    TypeScript to JavaScript:
    - Remove type annotations (e.g., 'const video: VideoClip' becomes 'const video')
    - Keep the actual method calls and properties the same
    """
    inputs = {
        "assets": {
            "type": "array",
            "description": "List of video assets to process. Default is the Big Buck Bunny sample.",
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

    def __init__(self):
        """Initialize the tool with empty state. State is populated in forward()."""
        super().__init__()
        self.page: Optional[Page] = None  # Browser page for editor
        self.browser: Optional[Browser] = None  # Remote browser instance
        self.output: Optional[str] = None  # Output video path
        self.assets: Optional[list[str]] = None  # Input video files
        logger.info("VideoEditorTool initialized")

    def save_chunk(self, data: list[int], position: int) -> None:
        """Writes the received video chunk at the specified position."""
        if not self.output:
            logger.error("Output path not set when trying to save chunk")
            raise ValueError("Output path not set")

        try:
            with open(self.output, "r+b") as f:
                f.seek(position)
                f.write(bytearray(data))
            logger.debug(f"Saved chunk of size {len(data)} at position {position}")
        except Exception as e:
            logger.error(f"Failed to save chunk: {str(e)}")
            raise

    def _ensure_output_directory(self, output_path: str) -> None:
        """Ensure the output directory exists."""
        output_dir = os.path.dirname(output_path)
        if output_dir:  # Only create if there's a directory part
            logger.debug(f"Creating output directory: {output_dir}")
            os.makedirs(output_dir, exist_ok=True)

    async def launch_editor(self, playwright: Playwright):
        """Connects to the remote browser with API key. And sets up the editor."""
        if not self.output or not self.assets:
            logger.error("Output path or assets not set when launching editor")
            raise ValueError("Output path or assets not set")

        try:
            # Ensure output directory exists
            self._ensure_output_directory(self.output)

            logger.info("Connecting to remote browser...")
            self.browser = await playwright.chromium.connect_over_cdp(
                "wss://chrome.diffusion.studio?token=d638be68e96471b515a8166161a3af1a9b6884e048120d6e9c3bcc1d135fa0da"
            )
            logger.debug("Connected to remote browser")

            self.page = await self.browser.new_page()
            logger.debug("Created new page")

            logger.info("Loading editor interface...")
            await self.page.goto("https://operator-ui.vercel.app")
            await self.page.wait_for_function("typeof window.core !== 'undefined'")
            logger.debug("Editor interface loaded")

            input = self.page.locator("#file-input")
            logger.info("Scripts loaded")

            self.page.on("console", lambda msg: logger.debug(f"[Browser]: {msg.text}"))
            await self.page.expose_function("saveChunk", self.save_chunk)
            logger.debug("Exposed save_chunk function to browser")

            logger.info(f"Setting input file: {self.assets[0]}")
            await input.set_input_files(self.assets[0])
            logger.debug("Input file set successfully")

        except Exception as e:
            logger.exception(f"Failed to launch editor: {str(e)}")
            raise

    async def evaluate(self, js_code: str):
        if not self.page:
            logger.error("Page not initialized when trying to evaluate JavaScript")
            raise ValueError("Page not initialized")

        try:
            logger.info("Evaluating JavaScript code...")
            logger.debug(f"JavaScript code:\n{js_code}")

            result = await self.page.evaluate(f"""
            async () => {{
                try {{
                    {js_code}
                    return 'success';
                }} catch (e) {{
                    console.error(e.message);
                    console.error(e.stack);
                    return 'error';
                }}
            }}
            """)
            logger.info(f"JavaScript evaluation result: {result}")
            return result
        except Exception as e:
            logger.exception(f"Failed to evaluate JavaScript: {str(e)}")
            raise

    def forward(
        self,
        assets: list[str] = ["assets/big_buck_bunny_1080p_30fps.mp4"],
        js_code: str = """
        // Default example: Create a 150 frames subclip
        const videoFile = assets()[0];
        const video = new core.VideoClip(videoFile).subclip(0, 150);
        await composition.add(video);
        await render();
        """,
        output: str = "output/video.mp4",
    ) -> Any:
        """Main execution method that processes the video editing task."""
        logger.info(f"Starting video editing task with assets: {assets}")
        logger.debug(f"Output path: {output}")

        # Always create a new event loop and run to completion
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            result = loop.run_until_complete(
                self._async_forward(assets, js_code, output)
            )
            logger.info("Video editing completed synchronously")
            return result
        finally:
            loop.close()
            logger.debug("Event loop closed")

    async def _async_forward(self, assets: list[str], js_code: str, output: str) -> str:
        """Async implementation of the forward method."""
        try:
            self.assets = assets
            self.output = output
            clear_file_path(output)
            logger.debug("State initialized")

            async with async_playwright() as playwright:
                try:
                    await self.launch_editor(playwright)
                    result = await self.evaluate(js_code)
                    logger.info("Video editing task completed successfully")
                    return result
                finally:
                    if self.browser:
                        logger.debug("Closing browser")
                        await self.browser.close()
        except Exception:
            logger.exception("Video editing task failed")
            raise
