import os
from dotenv import load_dotenv

load_dotenv()

MXBAI_API_URL = (
    "https://api-inference.huggingface.co/models/mixedbread-ai/mxbai-embed-large-v1"
)
EMBEDDING_DIM = 1024  # Dimension of embeddings from https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1/blob/main/config.json#L11
MXBAI_RERANK_URL = (
    "https://api-inference.huggingface.co/models/mixedbread-ai/mxbai-rerank-xsmall-v1"
)
HF_API_KEY = os.getenv("HUGGINGFACE_TOKEN")
MXBAI_HEADERS = {"Authorization": f"Bearer {HF_API_KEY}"}
COLLECTION_NAME = "docs"
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

DOCUMENT_CONTEXT_PROMPT = """
<document>
{doc_content}
</document>
"""

CHUNK_CONTEXT_PROMPT = """
Here is the chunk we want to situate within the whole document
<chunk>
{chunk_content}
</chunk>

Please give a short succinct context to situate this chunk within the overall document for the purposes of improving search retrieval of the chunk.
Answer only with the succinct context and nothing else.
"""

QUERY_PROMPT = "Represent this sentence for searching relevant passages: "

CUSTOM_SYSTEM_PROMPT = """You are a video editing assistant that helps users edit videos using DiffStudio's web-based editor.
You have access to two tools:
1. A video editor tool that can execute JavaScript code in the browser to manipulate videos
2. A documentation search tool to find examples and syntax for Diffusion Studio's video editing features

When editing videos:
- First search the docs to find the right syntax if you're unsure
- Convert any TypeScript code from docs to JavaScript (remove type annotations) before using it
- Use the video editor tool to execute the JavaScript code
- Handle errors gracefully and provide clear feedback
- Always verify the output path and input assets exist

Example workflow:
1. Search docs for the specific feature
2. Extract the relevant code and convert TypeScript to JavaScript
3. Adapt the code for the current task
4. Execute it using the video editor tool

TypeScript to JavaScript conversion example:
TypeScript:
```ts
const video: VideoClip = new core.VideoClip(file).subclip(0, 150);
const options: RenderOptions = { quality: "high" };
```
JavaScript:
```js
const video = new core.VideoClip(file).subclip(0, 150);
const options = { quality: "high" };
```
"""

MAX_RETRIES = 10
RETRY_DELAY = 10  # seconds
