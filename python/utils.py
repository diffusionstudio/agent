import os
import httpx
import asyncio
from loguru import logger
from anthropic import AsyncAnthropic
from anthropic.types import Usage, TextBlock
from config import (
    MXBAI_API_URL,
    MXBAI_HEADERS,
    MXBAI_RERANK_URL,
    ANTHROPIC_API_KEY,
    DOCUMENT_CONTEXT_PROMPT,
    CHUNK_CONTEXT_PROMPT,
    MAX_RETRIES,
    RETRY_DELAY,
)

client = AsyncAnthropic(api_key=ANTHROPIC_API_KEY)


def clear_file_path(output: str):
    """Clears the output path if it exists."""
    if os.path.exists(output):
        os.remove(output)
        print(f"Removed existing file: {output}")


def chunk_markdown(content: str, max_lines: int = 100) -> list[str]:
    """Split markdown into chunks of max_lines if needed."""
    lines = content.splitlines()
    if len(lines) <= max_lines:
        return [content]

    chunks = []
    for i in range(0, len(lines), max_lines):
        chunk = "\n".join(lines[i : i + max_lines])
        chunks.append(chunk)
    return chunks


async def generate_embeddings(text: str, timeout=30, retries=MAX_RETRIES):
    """
    Generate embeddings for the given text using MXBAI API.

    Args:
        text (str): Text to embed
        timeout (int, optional): Request timeout in seconds. Defaults to 30.
        retries (int, optional): Number of retries on failure. Defaults to MAX_RETRIES.

    Returns:
        dict: JSON response containing embeddings
    """
    last_error = None
    for attempt in range(retries):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    MXBAI_API_URL,
                    headers=MXBAI_HEADERS,
                    json={"inputs": text},
                    timeout=timeout,
                )
                response.raise_for_status()
                return response.json()
        except (httpx.TimeoutException, httpx.HTTPError) as e:
            last_error = e
            if attempt < retries - 1:
                delay = RETRY_DELAY * (attempt + 1)  # Exponential backoff
                logger.warning(
                    f"Embedding attempt {attempt + 1} failed: {str(e)}. Retrying in {delay}s..."
                )
                await asyncio.sleep(delay)
            continue

    if isinstance(last_error, httpx.TimeoutException):
        raise TimeoutError(f"Request timed out after {retries} attempts")
    raise RuntimeError(f"Request failed after {retries} attempts: {str(last_error)}")


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
        payload = {"inputs": [{"text": query, "text_pair": doc} for doc in documents]}
        async with httpx.AsyncClient() as client:
            response = await client.post(
                MXBAI_RERANK_URL, headers=MXBAI_HEADERS, json=payload, timeout=timeout
            )
            response.raise_for_status()
            return response.json()
    except httpx.TimeoutException:
        raise TimeoutError("Rerank request timed out")
    except httpx.HTTPError as e:
        raise RuntimeError(f"Rerank request failed: {str(e)}")


async def situate_context(
    doc: str, chunk: str, retries=MAX_RETRIES
) -> tuple[str, Usage]:
    """
    Uses Claude to understand where a chunk of text fits within a larger document context.

    Args:
        doc (str): The full document content
        chunk (str): The specific chunk to situate
        retries (int, optional): Number of retries on failure. Defaults to MAX_RETRIES.

    Returns:
        tuple[str, Usage]: Tuple of (response text, usage stats)
    """
    last_error = None
    for attempt in range(retries):
        try:
            response = await client.messages.create(
                model="claude-3-5-sonnet-latest",
                max_tokens=1024,
                temperature=0.0,
                system=[
                    {
                        "type": "text",
                        "text": DOCUMENT_CONTEXT_PROMPT.format(doc_content=doc),
                        "cache_control": {"type": "ephemeral"},
                    }
                ],
                messages=[
                    {
                        "role": "user",
                        "content": CHUNK_CONTEXT_PROMPT.format(chunk_content=chunk),
                    }
                ],
            )
            content_block = response.content[0]
            return content_block.text if isinstance(
                content_block, TextBlock
            ) else "", response.usage
        except Exception as e:
            last_error = e
            if attempt < retries - 1:
                delay = RETRY_DELAY * (attempt + 1)
                logger.warning(
                    f"Context generation attempt {attempt + 1} failed: {str(e)}. Retrying in {delay}s..."
                )
                await asyncio.sleep(delay)
            continue

    raise RuntimeError(
        f"Context generation failed after {retries} attempts: {str(last_error)}"
    )
