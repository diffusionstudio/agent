import os
from dotenv import load_dotenv
load_dotenv()

MXBAI_API_URL = "https://api-inference.huggingface.co/models/mixedbread-ai/mxbai-embed-large-v1"
MXBAI_RERANK_URL = "https://api-inference.huggingface.co/models/mixedbread-ai/mxbai-rerank-base-v1"
MXBAI_HEADERS = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_TOKEN')}"}
DB_CONNECTION = os.getenv('DB_CONNECTION')
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')

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
