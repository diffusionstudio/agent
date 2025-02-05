import os
import atexit

from playwright.sync_api import sync_playwright, Playwright, Page, Browser
from typing import Optional, List
from loguru import logger

from src.utils import clear_file_path
from src.settings import settings


class DiffusionClient:
    """Client for the Diffusion Studio editor."""

    # Private attributes
    _output: Optional[str] = None
    _assets: Optional[list[str]] = None

    # Public attributes
    browser: Browser
    page: Page
    samples: List[str] = []
    executable_path = settings.playwright_chromium_executable_path
    web_socket_url = settings.playwright_web_socket_url

    def __init__(self):
        """Initialize the Diffusion Studio client."""
        self.playwright = sync_playwright().start()
        self.init(self.playwright)
        atexit.register(self.close)  # Auto-close on exit

    def init(self, playwright: Playwright):
        """Connects to the remote browser with API key. And sets up the editor."""
        try:
            if self.web_socket_url:
                self.browser = playwright.chromium.connect_over_cdp(self.web_socket_url)
                logger.debug("Connected to remote browser via cdp")
            else:
                self.browser = playwright.chromium.launch(
                    executable_path=self.executable_path
                )
                logger.debug("Local browser launched")

            self.page = self.browser.new_page()

            logger.info("Loading editor interface...")
            self.page.goto(settings.url)
            self.page.wait_for_function("typeof window.core !== 'undefined'")
            logger.debug("Editor interface loaded")

            self.page.on("console", lambda msg: logger.debug(f"[Browser]: {msg.text}"))
            self.page.expose_function("saveChunk", self._save_chunk)
            logger.debug("Exposed save_chunk function to browser")

            self.page.expose_function("saveSample", self._save_sample)
            logger.debug("Exposed save_sample function to browser")

        except Exception as e:
            logger.exception(f"Failed to launch editor: {str(e)}")
            raise

    def _save_chunk(self, data: list[int], position: int) -> None:
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
        except Exception as e:
            logger.error(f"Failed to save chunk: {str(e)}")
            raise

    def _save_sample(self, data: str) -> None:
        """Saves a sample video to the output directory."""
        self.samples.append(data.replace("data:image/jpeg;base64,", ""))

    @property
    def output(self) -> Optional[str]:
        return self._output

    @output.setter
    def output(self, value: Optional[str]) -> None:
        if value:
            clear_file_path(value)
        self._output = value

    def evaluate(self, javascript: str) -> str:
        """Evaluates the JavaScript code in the browser."""

        self.samples = []  # Reset samples

        if not self.page:
            logger.error("Page not initialized when trying to evaluate JavaScript")
            raise ValueError("Page not initialized")

        try:
            logger.info("Client evaluating JavaScript code...")

            # Wrap the code in an async IIFE (Immediately Invoked Function Expression)
            wrapped_code = f"""
            (async () => {{
                try {{
                    {javascript}
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

    def upload_assets(self, assets: list[str]) -> None:
        """Uploads the assets to the editor."""

        # If the assets are the same as the previous ones, do nothing
        if assets == self._assets:
            return

        input_element = self.page.locator("#file-input")
        input_element.set_input_files(assets[0])

        self._assets = assets

    def close(self):
        """Closes the browser and playwright."""
        try:
            if hasattr(self, "browser") and self.browser:
                self.browser.close()
                logger.debug("Browser closed")
            if hasattr(self, "playwright") and self.playwright:
                self.playwright.stop()
                logger.debug("Playwright stopped")
        except Exception as e:
            logger.error(f"Error during cleanup: {str(e)}")
            # Suppress errors during shutdown
            pass
