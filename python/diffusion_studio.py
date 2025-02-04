import base64
import os
from playwright.sync_api import sync_playwright, Playwright, Page, Browser
from typing import Optional, cast
from loguru import logger
from config import settings


class DiffusionClient:
    """Client for the Diffusion Studio editor."""

    def __init__(self):
        """Initialize the Diffusion Studio client."""
        self.playwright: Playwright
        self.browser: Browser
        self.page: Page
        self.output: Optional[str] = None
        self.executable_path = settings.playwright_chromium_executable_path
        self.web_socket_url = settings.playwright_web_socket_url
        self.init()  # Auto-initialize

    def init(self):
        """Initialize the client"""
        self.playwright = sync_playwright().start()
        self.launch_editor(self.playwright)

    def save_chunk(self, data: list[int], position: int) -> None:
        """Writes the received video chunk at the specified position."""
        if not self.output:
            logger.error("Output path not set when trying to save chunk")
            raise ValueError("Output path not set")

        try:
            if not os.path.exists(self.output):
                with open(self.output, "wb") as f:
                    pass
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
            base64_data = data.replace("data:image/png;base64,", "")
            buffer = base64.b64decode(base64_data)

            output_dir = "./samples"
            os.makedirs(output_dir, exist_ok=True)
            logger.debug(f"Output directory: {output_dir}")

            sample_count = len(
                [f for f in os.listdir(output_dir) if f.startswith("sample-")]
            )
            sample_path = os.path.join(output_dir, f"sample-{sample_count}.png")
            logger.debug(f"Sample path: {sample_path}")

            with open(sample_path, "wb") as f:
                f.write(buffer)
            logger.debug(f"Saved sample image to {sample_path}")

            logger.debug(
                f"Content of {output_dir}: {os.listdir(os.path.join(os.path.dirname(__file__), output_dir))}"
            )

        except Exception as e:
            logger.error(f"Failed to save sample: {str(e)}")
            raise

    def _ensure_output_directory(self, output_path: str) -> None:
        """Ensure the output directory exists."""
        output_dir = os.path.dirname(output_path)
        if output_dir:
            logger.debug(f"Creating output directory: {output_dir}")
            os.makedirs(output_dir, exist_ok=True)

    def evaluate(self, js_code: str) -> str:
        """Evaluates the JavaScript code in the browser."""
        logger.info(f"Client received JS code: {js_code}")

        if not self.page:
            logger.error("Page not initialized when trying to evaluate JavaScript")
            raise ValueError("Page not initialized")

        try:
            logger.info("Client evaluating JavaScript code...")

            # Wrap the code in an async IIFE (Immediately Invoked Function Expression)
            wrapped_code = f"""
            (async () => {{
                try {{
                    {js_code}
                    return 'success';
                }} catch (e) {{
                    console.error(e.message);
                    console.error(e.stack);
                    return 'error: ' + e.message;
                }}
            }})()
            """

            result = self.page.evaluate(wrapped_code)

            if not isinstance(result, str):
                result = "error"

            logger.debug(f"JavaScript evaluation result: {result}")
            return result

        except Exception as e:
            return str(e)

    def launch_editor(self, playwright: Playwright):
        """Connects to the remote browser with API key. And sets up the editor."""
        try:
            if self.web_socket_url:
                logger.debug("Connecting to remote browser via websocket ...")
                self.browser = playwright.chromium.connect_over_cdp(self.web_socket_url)
                logger.debug("Connected to remote browser via websocket")
            else:
                logger.info("Launching local browser...")
                self.browser = playwright.chromium.launch(
                    executable_path=self.executable_path
                )
                logger.debug("Local browser launched")

            if not self.browser:
                raise Exception("Browser not initialized")

            page = self.browser.new_page()
            if not page:
                raise Exception("Page not created")
            self.page = cast(Page, page)

            logger.debug("Created new page")

            logger.info("Loading editor interface...")
            page = cast(Page, self.page)  # Type assertion for mypy
            page.goto("https://operator.diffusion.studio")
            page.wait_for_function("typeof window.core !== 'undefined'")
            logger.debug("Editor interface loaded")

            page.on("console", lambda msg: logger.debug(f"[Browser]: {msg.text}"))
            page.expose_function("saveChunk", self.save_chunk)
            logger.debug("Exposed save_chunk function to browser")

            page.expose_function("saveSample", self.save_sample)
            logger.debug("Exposed save_sample function to browser")

        except Exception as e:
            logger.exception(f"Failed to launch editor: {str(e)}")
            raise

    def close(self):
        """Closes the browser and playwright."""
        if self.browser:
            self.browser.close()
            logger.debug("Browser closed")
        if self.playwright:
            self.playwright.stop()
            logger.debug("Playwright stopped")
