from smolagents import CodeAgent, LiteLLMModel
from src.settings import settings
from src.prompts import get_system_prompt
from src.client import DiffusionClient
from src.tools import (
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

agent.run("Trim assets/big_buck_bunny_1080p_30fps.mp4 to 5 seconds")
