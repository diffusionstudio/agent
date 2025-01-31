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
QDRANT_PATH = "embeddings/vector_db"
COLLECTION_NAME = "diffusion_studio_docs"  # More specific name
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

MAX_RETRIES = 10
RETRY_DELAY = 10  # seconds
