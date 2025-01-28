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


def clear_file_path(path: str) -> None:
    """Clear a file path, creating directories if needed."""
    try:
        # Create directory if it doesn't exist
        directory = os.path.dirname(path)
        if directory:
            logger.debug(f"Ensuring directory exists: {directory}")
            os.makedirs(directory, exist_ok=True)

        # Remove file if it exists
        if os.path.exists(path):
            logger.debug(f"Removing existing file: {path}")
            os.remove(path)

        logger.debug(f"Path cleared: {path}")
    except Exception as e:
        logger.error(f"Failed to clear path {path}: {str(e)}")
        raise


def chunk_markdown(content: str, max_lines: int = 100) -> list[str]:
    """
    Split markdown into chunks of max_lines, preserving code blocks.
    Won't split in the middle of a code block.
    """
    lines = content.splitlines()
    if len(lines) <= max_lines:
        return [content]

    chunks = []
    current_chunk = []
    current_size = 0
    in_code_block = False
    code_fence = ""

    for line in lines:
        # Detect code block boundaries
        if line.startswith("```"):
            if not in_code_block:  # Start of code block
                in_code_block = True
                code_fence = line
            elif line.startswith(code_fence):  # End of code block
                in_code_block = False
                code_fence = ""

        current_chunk.append(line)
        current_size += 1

        # Create new chunk if we hit max size and we're not in a code block
        if current_size >= max_lines and not in_code_block:
            chunks.append("\n".join(current_chunk))
            current_chunk = []
            current_size = 0

    # Add remaining lines
    if current_chunk:
        chunks.append("\n".join(current_chunk))

    return chunks


async def generate_embeddings(text: str | list[str], timeout=30, retries=MAX_RETRIES):
    """
    Generate embeddings for the given text using MXBAI API.

    Args:
        text (str | list[str]): Text or list of texts to embed
        timeout (int, optional): Request timeout in seconds. Defaults to 30.
        retries (int, optional): Number of retries on failure. Defaults to MAX_RETRIES.

    Returns:
        list[list[float]]: List of embeddings for each input text
    """
    last_error = None
    for attempt in range(retries):
        try:
            async with httpx.AsyncClient() as client:
                logger.debug(
                    f"Making embedding request with {len(text) if isinstance(text, list) else 1} texts"
                )
                response = await client.post(
                    MXBAI_API_URL,
                    headers=MXBAI_HEADERS,
                    json={"inputs": text if isinstance(text, list) else [text]},
                    timeout=timeout,
                )
                response.raise_for_status()
                embeddings = response.json()
                logger.debug(f"Got response with status {response.status_code}")

                if not embeddings:
                    raise ValueError("Empty response from embedding API")

                return embeddings if isinstance(text, list) else embeddings[0]

        except httpx.TimeoutException as e:
            last_error = e
            logger.warning(f"Timeout during embedding attempt {attempt + 1}: {str(e)}")
        except httpx.RequestError as e:
            last_error = e
            logger.warning(
                f"Request error during embedding attempt {attempt + 1}: {str(e)}"
            )
        except Exception as e:
            last_error = e
            logger.warning(
                f"Unexpected error during embedding attempt {attempt + 1}: {str(e)}"
            )

        if attempt < retries - 1:
            delay = RETRY_DELAY * (attempt + 1)  # Exponential backoff
            logger.warning(
                f"Embedding attempt {attempt + 1} failed. Retrying in {delay}s..."
            )
            await asyncio.sleep(delay)
            continue

    error_msg = f"Request failed after {retries} attempts"
    if isinstance(last_error, httpx.TimeoutException):
        raise TimeoutError(f"{error_msg}: Timeout - {str(last_error)}")
    elif isinstance(last_error, httpx.RequestError):
        raise RuntimeError(f"{error_msg}: Request failed - {str(last_error)}")
    else:
        raise RuntimeError(f"{error_msg}: {str(last_error)}")


async def rerank(query: str, documents: list[str], timeout=30, retries=MAX_RETRIES):
    """
    Rerank documents based on relevance to query using MXBAI reranking API.

    Args:
        query (str): The query text to compare documents against
        documents (list[str]): List of document texts to rerank
        timeout (int, optional): Request timeout in seconds. Defaults to 30.
        retries (int, optional): Number of retries on failure. Defaults to MAX_RETRIES.

    Returns:
        list[float]: List of relevance scores between 0 and 1 for each document

    Raises:
        TimeoutError: If request times out after all retries
        RuntimeError: If request fails for any other reason after all retries
    """
    last_error = None
    for attempt in range(retries):
        try:
            payload = {
                "inputs": [{"text": query, "text_pair": doc} for doc in documents]
            }
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    MXBAI_RERANK_URL,
                    headers=MXBAI_HEADERS,
                    json=payload,
                    timeout=timeout,
                )
                response.raise_for_status()
                return response.json()
        except httpx.TimeoutException as e:
            last_error = e
            logger.warning(f"Timeout during reranking attempt {attempt + 1}: {str(e)}")
        except httpx.RequestError as e:
            last_error = e
            logger.warning(
                f"Request error during reranking attempt {attempt + 1}: {str(e)}"
            )
        except Exception as e:
            last_error = e
            logger.warning(
                f"Unexpected error during reranking attempt {attempt + 1}: {str(e)}"
            )

        if attempt < retries - 1:
            delay = RETRY_DELAY * (attempt + 1)  # Exponential backoff
            logger.warning(
                f"Reranking attempt {attempt + 1} failed. Retrying in {delay}s..."
            )
            await asyncio.sleep(delay)
            continue

    error_msg = f"Rerank request failed after {retries} attempts"
    if isinstance(last_error, httpx.TimeoutException):
        raise TimeoutError(f"{error_msg}: Timeout - {str(last_error)}")
    elif isinstance(last_error, httpx.RequestError):
        raise RuntimeError(f"{error_msg}: Request failed - {str(last_error)}")
    else:
        raise RuntimeError(f"{error_msg}: {str(last_error)}")


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
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": DOCUMENT_CONTEXT_PROMPT.format(doc_content=doc),
                                "cache_control": {"type": "ephemeral"},
                            }
                        ],
                    },
                    {
                        "role": "user",
                        "content": CHUNK_CONTEXT_PROMPT.format(chunk_content=chunk),
                    },
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
