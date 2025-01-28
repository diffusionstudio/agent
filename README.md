# Video Composer Agent

## Setup

```bash
pip install uv
```

```bash
uv add -r requirements.txt
```

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
# Embed all docs
uv run docs_embedder.py embed

# Debug mode (first 5 files only)
uv run docs_embedder.py embed --debug
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
