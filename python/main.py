from smolagents import CodeAgent, HfApiModel, CODE_SYSTEM_PROMPT
from core_tool import VideoEditorTool
from docs_embedder import DocsSearchTool, LLMContentTool
from config import HF_API_KEY

modified_system_prompt = (
    CODE_SYSTEM_PROMPT
    + """
You are a video editing assistant that helps users edit videos using Diffusion Studio library.

You should always refer to the LLMContentTool to get LLM-friendly content. This file offers brief background information, guidance, and links to detailed markdown files.

If the retrieved content is not enough, you should use the DocsSearchTool to search for more information about syntax of Diffusion Studio, and convert the retrieved codes from Typescript to Javascript, before passing it to the VideoEditorTool.

Example code to add a subclip to a video that is 150 seconds long:
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
        tools=[VideoEditorTool(), DocsSearchTool(), LLMContentTool()],
        model=HfApiModel(token=HF_API_KEY),
        system_prompt=modified_system_prompt,
    )
    agent.run(
        "Add a 150 second subclip to the video, assets/big_buck_bunny_1080p_30fps.mp4"
    )


if __name__ == "__main__":
    main()
