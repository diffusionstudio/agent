from config import settings
from typing import List, Dict, Optional, Union, Any
from smolagents import Tool
from utils import (
    ensure_collection_exists,
    auto_embed_pipeline,
    search_docs,
)


class DocsSearchTool(Tool):
    name = "docs_search_tool"
    description = "A tool that searches through Diffusion Studio's documentation to find relevant code examples and syntax."

    inputs = {
        "query": {
            "type": "string",
            "description": "The search query about DiffStudio's functionality (e.g. 'how to add text overlay' or 'video transitions')",
        },
        "limit": {
            "type": "integer",
            "description": "Maximum number of results to return",
            "nullable": True,
        },
        "filter_conditions": {
            "type": "object",
            "description": "Optional filters for specific documentation sections",
            "nullable": True,
        },
        "rerank_results": {
            "type": "boolean",
            "description": "Whether to use semantic reranking for more accurate results",
            "nullable": True,
        },
    }
    output_type = "array"

    def __init__(self):
        ensure_collection_exists()
        auto_embed_pipeline(url=f"{settings.url}/llms.txt", hash_file=settings.hash_file)

    def forward(
        self,
        query: str,
        limit: int = 5,
        filter_conditions: Optional[
            Dict[str, Union[str, int, float, List[str]]]
        ] = None,
        rerank_results: bool = False,
    ) -> Any:
        """Search for documentation snippets."""
        return search_docs(
            query=query,
            limit=limit,
            filter_conditions=filter_conditions,
            rerank_results=rerank_results,
        )
