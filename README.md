<p align="center">
  <img src="./docs/assets/banner.png" alt="Library Banner" style="aspect-ratio: 1200/500;width: 100%;" />
  <h1 align="center">Video Composer Agent</h1>
</p>

<p align="center">
  <a href="https://discord.com/invite/zPQJrNGuFB"><img src="https://img.shields.io/discord/1115673443141156924?style=flat&logo=discord&logoColor=fff&color=000000" alt="discord"></a>
  <a href="https://x.com/diffusionhq"><img src="https://img.shields.io/badge/Follow for-Updates-blue?color=000000&logo=X&logoColor=ffffff" alt="Static Badge"></a>
  <a href="https://www.ycombinator.com/companies/diffusion-studio"><img src="https://img.shields.io/badge/Combinator-F24-blue?color=000000&logo=ycombinator&logoColor=ffffff" alt="Static Badge"></a>
</p>
<br/>

## Setup

```bash
pip install uv
```

```bash
uv sync
```

or alternatively:

```bash
uv add -r requirements.txt
```

## Environment Variables

You will need to use the environment variables defined in `.env.example` to run Video Composer Agent. It's recommended you use Vercel Environment Variables for this, but a `.env` file is all that is necessary.

**Note:** You should not commit your `.env` file or it will expose secrets that will allow others to control access to your various OpenAI and authentication provider accounts.

## Run Agent

To run the main script:

```bash
uv run main.py
```

Feel free to modify the `main.py` script to add new tools and modify the agent's behavior.

## Documentation Search

The documentation search system provides semantic search capabilities for Diffusion Studio's documentation:

### Usage
```python
from src.tools.docs_search import DocsSearchTool

# Initialize search tool
docs_search = DocsSearchTool()

# Basic search
results = docs_search.forward(query="how to add text overlay")

# With reranking for more accurate results
results = docs_search.forward(query="how to add text overlay", rerank_results=True)

# Limit number of results
results = docs_search.forward(query="how to add text overlay", limit=10)

# With filters
results = docs_search.forward(
    query="video transitions",
    filter_conditions={"section": "video-effects"}
)
```

The search tool:
- Uses vector embeddings for fast semantic search
- Supports optional semantic reranking for higher accuracy
- Allows filtering by documentation sections
- Auto-embeds documentation from configured URL
- Maintains embedding cache with hash checking

## Development

See [CONTRIBUTING.md](./CONTRIBUTING.md) for development setup and guidelines.

## ToDos PRs Welcome

- [ ] Add [MCP](https://modelcontextprotocol.io/introduction) integration
    > MCP is an open protocol that standardizes how applications provide context to LLMs. Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect your devices to various peripherals and accessories, MCP provides a standardized way to connect AI models to different data sources and tools.
- [ ] Add [BM25](https://github.com/anthropics/anthropic-cookbook/blob/main/skills/contextual-embeddings/guide.ipynb) to `DocsSearchTool` to enable hybrid search
- [ ] Add support for video understanding models like [VideoLLaMA](https://github.com/DAMO-NLP-SG/VideoLLaMA3)
