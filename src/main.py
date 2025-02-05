from smolagents import CodeAgent, LiteLLMModel
from settings import settings
from prompts import get_system_prompt
from client import DiffusionClient
from tools import (
    DocsSearchTool,
    VideoEditorTool,
    VisualFeedbackTool,
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
agent.run("Trim assets/big_buck_bunny_1080p_30fps.mp4 to 150 frames")
