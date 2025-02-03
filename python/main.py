import asyncio
from smolagents import CodeAgent, LiteLLMModel
from core_tool import VideoEditorTool
from visual_feedback_tool import VisualFeedbackTool
from docs_embedder import DocsSearchTool, ensure_collection_exists, auto_embed_pipeline
from config import settings
from prompts import get_system_prompt
from diffusion_studio import DiffusionClient


async def init_docs():
    """Initialize docs collection and ensure latest content is embedded."""
    await ensure_collection_exists()

    # Run auto-embed to ensure latest docs

    await auto_embed_pipeline(url=settings.url, hash_file=settings.hash_file)


def main():
    """Initialize docs collection and embeddings"""
    asyncio.run(init_docs())
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
    agent.run("""
    1. Clip big buck bunny to 150 frames, add it to the composition and render the result
    2. Dont render just use `await sample()` first and wait for claude feedback
    3. After claude feedback, render the video and analyze the output video to verify smooth transitions and quality
    """)
    client.close()


if __name__ == "__main__":
    main()
