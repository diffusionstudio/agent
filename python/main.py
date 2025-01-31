from smolagents import CodeAgent, LiteLLMModel
from core_tool import VideoEditorTool
from docs_embedder import DocsSearchTool, ensure_collection_exists
from config import ANTHROPIC_API_KEY
from prompts import SYSTEM_PROMPT
import asyncio


async def init_docs():
    """Initialize docs collection and ensure latest content is embedded."""
    await ensure_collection_exists()
    # Run auto-embed to ensure latest docs
    from docs_embedder import auto_embed_pipeline

    await auto_embed_pipeline(
        url="https://operator-ui.vercel.app/llms.txt", hash_file="docs/content_hash.txt"
    )


def main():
    """Initialize docs collection and embeddings"""
    asyncio.run(init_docs())

    agent = CodeAgent(
        tools=[VideoEditorTool(), DocsSearchTool()],
        model=LiteLLMModel(
            "anthropic/claude-3-5-sonnet-latest",
            temperature=0.0,
            api_key=ANTHROPIC_API_KEY,
        ),
        system_prompt=SYSTEM_PROMPT,
    )
    agent.run(
        "Animate assets/big_buck_bunny_1080p_30fps.mp4, it should be scaled to 50% in the beginning and 100% after a few seconds. Make sure it's centered. Add a text 'Hello World' at the bottom of the video. Then render the result."
    )


if __name__ == "__main__":
    main()
