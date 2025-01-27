import os
import httpx
from anthropic import AsyncAnthropic
from anthropic.types import Usage, TextBlock
from config import MXBAI_API_URL, MXBAI_HEADERS, MXBAI_RERANK_URL, ANTHROPIC_API_KEY, DOCUMENT_CONTEXT_PROMPT, CHUNK_CONTEXT_PROMPT

client = AsyncAnthropic(api_key=ANTHROPIC_API_KEY)

def clear_file_path(output: str):
    """Clears the output path if it exists."""
    if os.path.exists(output):
        os.remove(output)
        print(f"Removed existing file: {output}")

async def generate_embeddings(payload, timeout=30):
    """
    Generate embeddings for the given text using MXBAI API.
    
    Args:
        payload (dict): Request payload containing text to embed
        timeout (int, optional): Request timeout in seconds. Defaults to 30.
    
    Returns:
        dict: JSON response containing embeddings
        
    Raises:
        TimeoutError: If request times out
        RuntimeError: If request fails for any other reason
    """
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
    Rerank documents based on relevance to query using MXBAI reranking API.
    
    Args:
        query (str): The query text to compare documents against
        documents (list[str]): List of document texts to rerank
        timeout (int, optional): Request timeout in seconds. Defaults to 30.
    
    Returns:
        list[float]: List of relevance scores between 0 and 1 for each document
        
    Raises:
        TimeoutError: If request times out
        RuntimeError: If request fails for any other reason
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

async def situate_context(doc: str, chunk: str) -> tuple[str, Usage]:
    """
    Uses Claude to understand where a chunk of text fits within a larger document context.
    
    Args:
        doc (str): The full document content
        chunk (str): The specific chunk to situate
        
    Returns:
        tuple[str, Usage]: Tuple of (response text, usage stats)
    """
    response = await client.messages.create(
        model="claude-3-5-sonnet-latest",
        max_tokens=1024,
        temperature=0.0,
        system=[
            {
                "type": "text",
                "text": DOCUMENT_CONTEXT_PROMPT.format(doc_content=doc),
                "cache_control": {"type": "ephemeral"}
            }
        ],
        messages=[{
            "role": "user", 
            "content": CHUNK_CONTEXT_PROMPT.format(chunk_content=chunk)
        }]
    )
    content_block = response.content[0]
    return content_block.text if isinstance(content_block, TextBlock) else "", response.usage