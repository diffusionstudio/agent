import os
from dotenv import load_dotenv

load_dotenv()

MXBAI_API_URL = (
    "https://api-inference.huggingface.co/models/mixedbread-ai/mxbai-embed-large-v1"
)
EMBEDDING_DIM = 1024  # Dimension of embeddings from https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1/blob/main/config.json#L11
MXBAI_RERANK_URL = (
    "https://api-inference.huggingface.co/models/mixedbread-ai/mxbai-rerank-base-v1"
)
MXBAI_HEADERS = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_TOKEN')}"}
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

MAX_RETRIES = 10
RETRY_DELAY = 10  # seconds
