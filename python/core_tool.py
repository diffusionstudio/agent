import os
import asyncio
import base64

from playwright.async_api import async_playwright, Playwright, Page, Browser
from utils import clear_file_path
from smolagents import Tool
from typing import Optional, Any
from loguru import logger


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

    def __init__(self):
        """Initialize the tool with empty state. State is populated in forward()."""
        super().__init__()
        self.page: Optional[Page] = None  # Browser page for editor
        self.browser: Optional[Browser] = None  # Remote browser instance
        self.output: Optional[str] = None  # Output video path
        self.assets: Optional[list[str]] = None  # Input video files
        self.executable_path = os.getenv("PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH") # Path to the browser executable
        self.web_socket_url = os.getenv("PLAYWRIGHT_WEB_SOCKET_URL") # Web socket url to connect to the browser
        logger.info("VideoEditorTool initialized")

    def save_chunk(self, data: list[int], position: int) -> None:
        """Writes the received video chunk at the specified position."""
        if not self.output:
            logger.error("Output path not set when trying to save chunk")
            raise ValueError("Output path not set")

        try:
            # Create file if it doesn't exist
            if not os.path.exists(self.output):
                with open(self.output, "wb") as f:
                    pass  # Create empty file
                logger.debug(f"Created empty output file: {self.output}")

            with open(self.output, "r+b") as f:
                f.seek(position)
                f.write(bytearray(data))
            logger.debug(f"Saved chunk of size {len(data)} at position {position}")
        except Exception as e:
            logger.error(f"Failed to save chunk: {str(e)}")
            raise

    def save_sample(self, data: str) -> None:
        """Saves a sample video to the output directory."""
        
        try:
            # Remove the data URL prefix and decode base64
            base64_data = data.replace('data:image/png;base64,', '')
            buffer = base64.b64decode(base64_data)
            
            # Get output directory and create if it doesn't exist
            output_dir = './samples'
            os.makedirs(output_dir, exist_ok=True)
            
            # Generate sample filename
            sample_count = len([f for f in os.listdir(output_dir) if f.startswith('sample-')])
            sample_path = os.path.join(output_dir, f'sample-{sample_count}.png')
            
            # Save to filesystem
            with open(sample_path, 'wb') as f:
                f.write(buffer)
            
            logger.debug(f"Saved sample image to {sample_path}")
            
        except Exception as e:
            logger.error(f"Failed to save sample: {str(e)}")
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

            if self.web_socket_url:
                logger.info("Connecting to remote browser...")
                self.browser = await playwright.chromium.connect_over_cdp(self.web_socket_url)
                logger.debug("Connected to remote browser")
            else:
                logger.info("Launching local browser...")
                self.browser = await playwright.chromium.launch(executable_path=self.executable_path)
                logger.debug("Local browser launched")

            self.page = await self.browser.new_page()
            logger.debug("Created new page")

            logger.info("Loading editor interface...")
            await self.page.goto("https://operator.diffusion.studio")
            await self.page.wait_for_function("typeof window.core !== 'undefined'")
            logger.debug("Editor interface loaded")

            input = self.page.locator("#file-input")
            logger.info("Received file input reference:", bool(input))

            self.page.on("console", lambda msg: logger.debug(f"[Browser]: {msg.text}"))
            await self.page.expose_function("saveChunk", self.save_chunk)
            await self.page.expose_function("saveSample", self.save_sample)
            logger.debug("Exposed save_chunk function to browser")

            logger.info(f"Setting input file: {self.assets[0]}")
            await input.set_input_files(self.assets[0])
            logger.debug("Input file set successfully")

        except Exception as e:
            logger.exception(f"Failed to launch editor: {str(e)}")
            raise

    async def evaluate(self, js_code: str, max_retries: int = 3) -> str:
        if not self.page:
            logger.error("Page not initialized when trying to evaluate JavaScript")
            raise ValueError("Page not initialized")

        last_error = None
        for attempt in range(max_retries):
            try:
                logger.info(
                    f"Evaluating JavaScript code... (attempt {attempt + 1}/{max_retries})"
                )
                logger.debug(f"JavaScript code:\n{js_code}")

                result = await self.page.evaluate(
                    f"""
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
                """
                )

                if not isinstance(result, str):
                    result = "error"

                logger.info(f"JavaScript evaluation result: {result}")
                return result
            except Exception as e:
                last_error = e
                logger.warning(f"Attempt {attempt + 1} failed: {str(e)}")
                if attempt < max_retries - 1:
                    # Reinitialize page if needed
                    if "context was destroyed" in str(e):
                        logger.info("Reinitializing page due to destroyed context...")
                        if self.page:
                            await self.page.reload()
                            await self.page.wait_for_function(
                                "typeof window.core !== 'undefined'"
                            )
                            await self.page.expose_function(
                                "saveChunk", self.save_chunk
                            )
                            input = self.page.locator("#file-input")
                            if self.assets:
                                await input.set_input_files(self.assets[0])
                            continue
                    logger.exception(
                        f"Failed to evaluate JavaScript after {max_retries} attempts"
                    )

        raise RuntimeError(
            f"Failed to evaluate JavaScript after {max_retries} attempts: {str(last_error)}"
        )

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
