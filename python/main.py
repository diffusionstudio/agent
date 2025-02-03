from smolagents import CodeAgent, LiteLLMModel
from core_tool import VideoEditorTool
from visual_feedback_tool import VisualFeedbackTool
from docs_embedder import DocsSearchTool, ensure_collection_exists
from config import ANTHROPIC_API_KEY
from prompts import get_system_prompt
import asyncio


async def init_docs():
    """Initialize docs collection and ensure latest content is embedded."""
    await ensure_collection_exists()
    # Run auto-embed to ensure latest docs
    from docs_embedder import auto_embed_pipeline

    await auto_embed_pipeline(
        url="https://operator.diffusion.studio/llms.txt", hash_file="docs/content_hash.txt"
    )


def main():
    """Initialize docs collection and embeddings"""
    asyncio.run(init_docs())

    agent = CodeAgent(
        tools=[VideoEditorTool(), DocsSearchTool(), VisualFeedbackTool()],
        model=LiteLLMModel(
            "anthropic/claude-3-5-sonnet-latest",
            temperature=0.0,
            api_key=ANTHROPIC_API_KEY,
        ),
        system_prompt=get_system_prompt(),
    )

    # Example of using both tools in sequence
    agent.run("""
    1. Clip big buck bunny to 150 frames, add it to the composition and render the result
    2. After rendering, analyze the output video to verify smooth transitions and quality
    """)


if __name__ == "__main__":
    main()
