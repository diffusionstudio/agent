from playwright.async_api import async_playwright, Playwright, Page, Browser
from utils import clear_file_path


class Agent:
    page: Page
    browser: Browser
    output: str
    llm: None
    assets: list[str]
    task: str

    def __init__(
        self, assets: list[str], task: str, llm, output: str = "output/video.mp4"
    ):
        self.assets = assets
        self.task = task
        self.llm = llm
        self.output = output
        clear_file_path(output)

    def save_chunk(self, data: list[int], position: int) -> None:
      """Writes the received video chunk at the specified position."""
      with open(self.output, "r+b") as f:
          f.seek(position)
          f.write(bytearray(data))

    async def launch_editor(self, playwright: Playwright):
        """Connects to the remote browser with API key. And sets up the editor."""

        self.browser = await playwright.chromium.connect_over_cdp(
            "wss://chrome.diffusion.studio?token=d638be68e96471b515a8166161a3af1a9b6884e048120d6e9c3bcc1d135fa0da"
        )
        # Create a new page directly from browser
        self.page = await self.browser.new_page()

        # Pre-allocate output file
        with open(self.output, "wb") as f:
            # 100MB pre-allocation
            f.truncate(1024 * 1024 * 100)

        await self.page.goto("https://operator-ui.vercel.app")

        # Wait for scripts to load
        await self.page.wait_for_function("typeof window.core !== 'undefined'")

        input = self.page.locator("#file-input")
        print("Scripts loaded")

        # Add console listener
        self.page.on("console", lambda msg: print(f"[Browser]: {msg.text}"))

        # Expose save_chunk function to be used within the page
        await self.page.expose_function("saveChunk", self.save_chunk)

        # Set input files from assets
        await input.set_input_files(self.assets[0])  # Currently using first asset

    async def evaluate(self, javascript: str):
        return await self.page.evaluate(f"""
        async () => {{
            try {{
                {javascript}
                return 'success';
            }} catch (e) {{
                console.error(e.message);
                console.error(e.stack);
                return 'error';
            }}
        }}
        """)

    async def run(self):
        async with async_playwright() as playwright:
            try:
                # Connect to the remote browser with API key
                await self.launch_editor(playwright)

                # Define JavaScript function for video processing
                javascript = """
                const [videoFile] = files();
                const video = new core.VideoClip(videoFile).subclip(0, 150);
                await composition.add(video);
                await render();
                """

                result = await self.evaluate(javascript)

                # Here you can add logic to use self.llm for the task
                # For example: response = await self.llm.predict(self.task)

                return result

            finally:
                await self.browser.close()
