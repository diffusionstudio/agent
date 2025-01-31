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
uv add -r requirements.txt
```

## Environment Variables

Create a `.env` file with the following variables:
```
ANTHROPIC_API_KEY=sk-ant-...
HUGGINGFACE_TOKEN=hf_...
# Make sure the browser supports common audio/video codecs
PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
# Alternatively, you can use a remote browser (connect over cdp)
# PLAYWRIGHT_WEB_SOCKET_URL=ws://localhost:3000
```

## ToDos

- [X] Add auto-embedding of new docs
    - Add a tool to fetch the latest docs from the operator-ui repo
    - Checks hash of the file to see if it has changed
    - If it has changed, parse `---` as chunks feed into embed pipeline
    - If it has not changed, skip embedding and just use the existing vector db
- [ ] Add [BM25](https://github.com/anthropics/anthropic-cookbook/blob/main/skills/contextual-embeddings/guide.ipynb) to enable hybrid search
- [ ] Add [MCP](https://modelcontextprotocol.io/introduction) integration
    > MCP is an open protocol that standardizes how applications provide context to LLMs. Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect your devices to various peripherals and accessories, MCP provides a standardized way to connect AI models to different data sources and tools.
    Also see: [Simple Chatbot](https://github.com/modelcontextprotocol/python-sdk/tree/main/examples/clients/simple-chatbot)
- [ ] Add DAPI support for speech recognition and synthesis workloads
- [ ] Add [VideoLLaMA](https://github.com/DAMO-NLP-SG/VideoLLaMA3) support
- [ ] Add State management for VideoEditor Tool
- [ ] Reuse browser session for forward steps and render the composition when editing instructions are fulfilled
- [ ] Feed [browser session recording](https://playwright.dev/python/docs/videos) back to video undertanding model and enable agent to call pause/play/seek


## Run Agent

To run the main script:

```bash
cd python
uv run main.py
```

Feel free to modify the `main.py` script to add new tools and modify the agent's behavior.

## Documentation Search & Evaluation

The `docs_embedder.py` script provides tools for embedding, searching, and evaluating documentation:

### Embed Documentation
```bash
# Auto-embed from URL (default: operator-ui.vercel.app/llms.txt)
uv run docs_embedder.py auto-embed

# Debug mode (first 5 chunks only)
uv run docs_embedder.py auto-embed --debug

# Force update embeddings (ignore hash check)
uv run docs_embedder.py auto-embed --force

# Custom URL and hash file
uv run docs_embedder.py auto-embed --url "https://your-url.com/docs.txt" --hash-file "path/to/hash.txt"
```

### Search Documentation
```bash
# Basic search
uv run docs_embedder.py search "how to add text overlay"

# With reranking (more accurate)
uv run docs_embedder.py search --rerank "how to add text overlay"

# Limit results
uv run docs_embedder.py search --limit 10 "how to add text overlay"

# Show full content
uv run docs_embedder.py search --full-content "how to add text overlay"

# Filter by file
uv run docs_embedder.py search --filepath "video-clip.md" "how to trim video"
```

### Evaluate Search Quality
```bash
# Run evaluation on QnA pairs
uv run docs_embedder.py eval
```

The eval command:
- Tests search against known question/answer pairs
- Compares vector search vs reranking
- Shows metrics like accuracy, rank@1, and semantic matches
- Displays detailed results for each query
