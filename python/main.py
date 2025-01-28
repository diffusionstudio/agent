from smolagents import CodeAgent, HfApiModel, CODE_SYSTEM_PROMPT
from core_tool import VideoEditorTool
from docs_embedder import DocsSearchTool, ensure_collection_exists
from config import HF_API_KEY
import asyncio

modified_system_prompt = (
    CODE_SYSTEM_PROMPT
    + """
You are a video editing assistant that helps users edit videos using Diffusion Studio library.

If the retrieved content is not enough, you should use the DocsSearchTool to search for more information about syntax of Diffusion Studio, and convert the retrieved codes from Typescript to Javascript, before passing it to the VideoEditorTool.

Sample code for adding to a video, clipping it to 150 frames and then rendering the composition:
```js
const videoFile = assets()[0];
const video = new core.VideoClip(videoFile).subclip(0, 150);
await composition.add(video);
await render();
```
"""
)


async def init_docs():
    """Initialize docs collection."""
    await ensure_collection_exists()


def main():
    # Initialize docs collection
    asyncio.run(init_docs())

    agent = CodeAgent(
        tools=[VideoEditorTool(), DocsSearchTool()],
        model=HfApiModel(token=HF_API_KEY),
        system_prompt=modified_system_prompt,
    )
    agent.run(
        "Clip big buck bunny to 150 frames, add it to the composition and render the result"
    )


if __name__ == "__main__":
    main()
