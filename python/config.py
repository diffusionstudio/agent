import os
from dotenv import load_dotenv

load_dotenv()

EMBEDDING_DIM = 1024
INFINITY_BASE_URL = "https://muhtasham--infinity-serve.modal.run"
INFINITY_API_KEY = "sk-dummy"

QDRANT_PATH = "embeddings/vector_db"
COLLECTION_NAME = "diffusion_studio_docs"
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH = os.getenv("PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH")

MAX_RETRIES = 10
RETRY_DELAY = 10  # seconds
