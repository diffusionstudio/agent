import os
import httpx
from config import MXBAI_API_URL, MXBAI_HEADERS, MXBAI_RERANK_URL

def clear_file_path(output: str):
    """Clears the output path if it exists."""
    if os.path.exists(output):
        os.remove(output)
        print(f"Removed existing file: {output}")

async def generate_embeddings(payload, timeout=30):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                MXBAI_API_URL,
                headers=MXBAI_HEADERS,
                json=payload,
                timeout=timeout
            )
            response.raise_for_status()
            return response.json()
    except httpx.TimeoutException:
        raise TimeoutError("Request timed out")
    except httpx.HTTPError as e:
        raise RuntimeError(f"Request failed: {str(e)}")

async def rerank(query: str, documents: list[str], timeout=30):
    """
    Rerank documents based on relevance to query.
    Returns list of scores between 0 and 1.
    """
    try:
        payload = {
            "inputs": [
                {"text": query, "text_pair": doc} 
                for doc in documents
            ]
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(
                MXBAI_RERANK_URL,
                headers=MXBAI_HEADERS,
                json=payload,
                timeout=timeout
            )
            response.raise_for_status()
            return response.json()
    except httpx.TimeoutException:
        raise TimeoutError("Rerank request timed out")
    except httpx.HTTPError as e:
        raise RuntimeError(f"Rerank request failed: {str(e)}")