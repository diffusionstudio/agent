from smolagents import CodeAgent, LiteLLMModel
from config import settings
from prompts import get_system_prompt
from diffusion_studio import DiffusionClient
from diffusiton_studio_tools import (
    VideoEditorTool,
    VisualFeedbackTool,
    DocsSearchTool,
)

client = DiffusionClient()

agent = CodeAgent(
    tools=[
        DocsSearchTool(),
        VideoEditorTool(client=client),
        VisualFeedbackTool(client=client),
    ],
    model=LiteLLMModel(
        "anthropic/claude-3-5-sonnet-latest",
        temperature=0.0,
        api_key=settings.anthropic_api_key,
    ),
    system_prompt=get_system_prompt(),
)

# Example of using both tools in sequence
agent.run(
    """
    Your goal is to clip big buck bunny to 150 frames, add it to the composition and render the result, assets/big_buck_bunny_1080p_30fps.mp4
    """
)
