import os
import asyncio
from playwright.async_api import async_playwright, Playwright

OUTPUT_FILE = "output/video.mp4"

# Remove output file if it exists
if os.path.exists(OUTPUT_FILE):
    os.remove(OUTPUT_FILE)
    print(f"Removed existing file: {OUTPUT_FILE}")


def save_chunk(data: list[int], position: int) -> None:
    """Writes the received video chunk at the specified position."""
    with open(OUTPUT_FILE, "r+b") as f:
        f.seek(position)
        f.write(bytearray(data))


# Define JavaScript function
js_function = """
async () => {
    try {
        const [videoFile] = files();
        const video = new core.VideoClip(videoFile).subclip(0, 150);
        await composition.add(video);
        await render();
        return 0;
    } catch (e) {
        console.error(e.message);
        console.error(e.stack);
        return 1;
    }
}
"""


async def run(playwright: Playwright):
    # Connect to the remote browser with API key
    browser = await playwright.chromium.connect_over_cdp(
        "wss://chrome.diffusion.studio?token=d638be68e96471b515a8166161a3af1a9b6884e048120d6e9c3bcc1d135fa0da"
    )

    # Create a new page directly from browser
    page = await browser.new_page()

    # Pre-allocate a file
    with open(OUTPUT_FILE, "wb") as f:
        # 100MB pre-allocation
        f.truncate(1024 * 1024 * 100)

    await page.goto("https://operator-ui.vercel.app")

    # Wait for scripts to load
    await page.wait_for_function("typeof window.core !== 'undefined'")

    input = page.locator("#file-input")

    print("Scripts loaded")

    # Add console listener
    page.on("console", lambda msg: print(f"[Browser]: {msg.text}"))

    # Expose save_chunk function to be used within the page
    await page.expose_function("saveChunk", save_chunk)

    await input.set_input_files("./assets/big_buck_bunny_1080p_30fps.mp4")

    result = await page.evaluate(js_function)
    print("result:", result)

    return browser


if __name__ == "__main__":
    async def main():
        async with async_playwright() as playwright:
            browser = await run(playwright)
            await browser.close()

    asyncio.run(main())
