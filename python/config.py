import os
from dotenv import load_dotenv
load_dotenv()

MXBAI_API_URL = "https://api-inference.huggingface.co/models/mixedbread-ai/mxbai-embed-large-v1"
MXBAI_RERANK_URL = "https://api-inference.huggingface.co/models/mixedbread-ai/mxbai-rerank-base-v1"
MXBAI_HEADERS = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_TOKEN')}"}
