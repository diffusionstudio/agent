from smolagents import CodeAgent, HfApiModel, CODE_SYSTEM_PROMPT
from core_tool import VideoEditorTool
from docs_embedder import DocsSearchTool
from config import HF_API_KEY

modified_system_prompt = (
    CODE_SYSTEM_PROMPT
    + """
You are a video editing assistant that helps users edit videos using Diffusion Studio's web-based editor.

Example code:
```js
const [videoFile] = files();
const video = new core.VideoClip(videoFile).subclip(0, 150);
await composition.add(video);
await render();
```
"""
)


def main():
    agent = CodeAgent(
        tools=[VideoEditorTool(), DocsSearchTool()],
        model=HfApiModel(token=HF_API_KEY),
        system_prompt=modified_system_prompt,
    )
    agent.run(
        "Add a 150 second subclip to the video, assets/big_buck_bunny_1080p_30fps.mp4"
    )


if __name__ == "__main__":
    main()
