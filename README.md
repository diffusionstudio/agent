# Video Composer Agent

## Setup

```bash
pip install uv
```

```bash
uv add -r requirements.txt
```

## ToDos

- [X] Add auto-embedding of new docs
    - Add a tool to fetch the latest docs from the operator-ui repo
    - Checks hash of the file to see if it has changed
    - If it has changed, parse `---` as chunks feed into embed pipeline
    - If it has not changed, skip embedding and just use the existing vector db
- [ ] Add BM25 to enable hybrid search

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
