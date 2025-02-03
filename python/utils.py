import os
import httpx
import asyncio
from loguru import logger
from anthropic import AsyncAnthropic
from anthropic.types import Usage, TextBlock
from openai import AsyncOpenAI
from config import (
    INFINITY_BASE_URL,
    INFINITY_API_KEY,
    ANTHROPIC_API_KEY,
    MAX_RETRIES,
    RETRY_DELAY,
)
from prompts import DOCUMENT_CONTEXT_PROMPT, CHUNK_CONTEXT_PROMPT
from pathlib import Path
from typing import List, Dict
from rich.console import Console
from rich.panel import Panel
import re

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


async def generate_embeddings(text: str | list[str], timeout=30, retries=MAX_RETRIES):
    """
    Generate embeddings for the given text using Infinity API.

    Args:
        text (str | list[str]): Text or list of texts to embed
        timeout (int, optional): Request timeout in seconds. Defaults to 30.
        retries (int, optional): Number of retries on failure. Defaults to MAX_RETRIES.

    Returns:
        list[list[float]]: List of embeddings for each input text
    """
    client = AsyncOpenAI(api_key=INFINITY_API_KEY, base_url=INFINITY_BASE_URL)
    last_error = None

    for attempt in range(retries):
        try:
            logger.debug(
                f"Making embedding request with {len(text) if isinstance(text, list) else 1} texts"
            )
            response = await client.embeddings.create(
                model="mixedbread-ai/mxbai-embed-large-v1",
                input=text if isinstance(text, list) else [text],
            )
            embeddings = [data.embedding for data in response.data]
            logger.debug("Got embeddings successfully")
            return embeddings if isinstance(text, list) else embeddings[0]

        except Exception as e:
            last_error = e
            logger.warning(f"Error during embedding attempt {attempt + 1}: {str(e)}")

            if attempt < retries - 1:
                delay = RETRY_DELAY * (attempt + 1)  # Exponential backoff
                logger.warning(
                    f"Embedding attempt {attempt + 1} failed. Retrying in {delay}s..."
                )
                await asyncio.sleep(delay)
                continue

    error_msg = f"Request failed after {retries} attempts"
    raise RuntimeError(f"{error_msg}: {str(last_error)}")


async def rerank(query: str, documents: list[str], timeout=30, retries=MAX_RETRIES):
    """
    Rerank documents based on relevance to query using Infinity reranking API.

    Args:
        query (str): The query text to compare documents against
        documents (list[str]): List of document texts to rerank
        timeout (int, optional): Request timeout in seconds. Defaults to 30.
        retries (int, optional): Number of retries on failure. Defaults to MAX_RETRIES.

    Returns:
        list[float]: List of relevance scores between 0 and 1 for each document
    """
    last_error = None
    for attempt in range(retries):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{INFINITY_BASE_URL}/rerank",
                    json={
                        "model": "mixedbread-ai/mxbai-rerank-base-v1",
                        "query": query,
                        "documents": documents,
                    },
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


def normalize_code(text: str) -> str:
    """Normalize code by removing comments, whitespace, and other non-essential elements."""
    # Remove code block markers
    text = text.replace("```javascript\n", "").replace("```\n", "").replace("```", "")
    # Remove comments
    text = re.sub(r"//.*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.DOTALL)
    # Remove empty lines and normalize whitespace
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    return "\n".join(lines)


def normalize_path(path: str) -> str:
    """Normalize a file path for comparison."""
    # Convert to Path object and resolve
    path = Path(path).as_posix()
    # Remove leading/trailing slashes
    path = path.strip("/")
    # Convert to lowercase for case-insensitive comparison
    return path.lower()


def print_results(title: str, results: List[Dict]):
    console = Console()
    console.print(f"\n[bold cyan]{title}[/bold cyan]")

    def crop_text(text: str, max_length: int = 500) -> str:
        if not text:
            return "Not found"
        text = text.strip()
        if len(text) > max_length:
            return text[:max_length] + "..."
        return text

    for result in results:
        # Create panel for each result
        content = [
            f"[bold]{result['id']}: {result['question']}[/bold]",
            f"[green]Reference: {result['reference']}[/green]",
            f"Found: {'✓' if result['reference_found'] else '✗'} (Rank: {result['reference_rank'] if result['reference_found'] else '-'})",
            f"Search Score: {result['top_score']:.3f}",
            "",
            "[bold]Reference Answer:[/bold]",
            crop_text(result.get("reference_answer", "")),
            "",
            "[bold]Found Content:[/bold]",
            crop_text(result.get("found_content", "")),
            "",
            "[bold]Similarity Scores:[/bold]",
            f"Text: {result.get('semantic_score', 0.0):.3f} ({'✓' if result.get('semantic_match', False) else '✗'})",
            f"Code: {result.get('code_score', 0.0):.3f} ({'✓' if result.get('code_match', False) else '✗'})",
        ]

        if "error" in result:
            content.append(f"[red]Error: {result['error']}[/red]")

        panel = Panel(
            "\n".join(content),
            title=f"Q{result['id']}",
            title_align="left",
            border_style="blue",
        )
        console.print(panel)

    return get_summary_metrics(results)


def get_summary_metrics(results: List[Dict]) -> Dict:
    total = len(results)
    found = sum(1 for r in results if r["reference_found"])
    rank_1 = sum(1 for r in results if r["reference_rank"] == 1)
    text_matches = sum(1 for r in results if r.get("semantic_match", False))
    code_matches = sum(1 for r in results if r.get("code_match", False))
    avg_score = sum(r["top_score"] for r in results) / total if total > 0 else 0
    avg_text = (
        sum(r.get("semantic_score", 0) for r in results) / total if total > 0 else 0
    )
    avg_code = sum(r.get("code_score", 0) for r in results) / total if total > 0 else 0
    errors = sum(1 for r in results if "error" in r)

    return {
        "total": total,
        "found": found,
        "rank_1": rank_1,
        "text_matches": text_matches,
        "code_matches": code_matches,
        "avg_score": avg_score,
        "avg_text": avg_text,
        "avg_code": avg_code,
        "errors": errors,
    }


def print_comparison(no_rerank_metrics: Dict, rerank_metrics: Dict):
    console = Console()
    console.print("\n[bold cyan]Performance Comparison[/bold cyan]")

    total = no_rerank_metrics["total"]

    def format_metric(
        name: str, vector_val: float, rerank_val: float, is_percent: bool = True
    ):
        if is_percent:
            vector_str = f"{vector_val / total * 100:.1f}%"
            rerank_str = f"{rerank_val / total * 100:.1f}%"
            diff = (rerank_val - vector_val) / total * 100
        else:
            vector_str = f"{vector_val:.3f}"
            rerank_str = f"{rerank_val:.3f}"
            diff = rerank_val - vector_val

        diff_color = "green" if diff > 0 else "red" if diff < 0 else "white"
        diff_str = f"[{diff_color}]{'+' if diff > 0 else ''}{diff:.1f}{'%' if is_percent else ''}[/{diff_color}]"

        return f"[bold]{name}:[/bold]\n  Vector: {vector_str}\n  Rerank: {rerank_str}\n  Diff: {diff_str}"

    metrics = [
        format_metric(
            "References Found", no_rerank_metrics["found"], rerank_metrics["found"]
        ),
        format_metric("Rank@1", no_rerank_metrics["rank_1"], rerank_metrics["rank_1"]),
        format_metric(
            "Text Matches",
            no_rerank_metrics["text_matches"],
            rerank_metrics["text_matches"],
        ),
        format_metric(
            "Code Matches",
            no_rerank_metrics["code_matches"],
            rerank_metrics["code_matches"],
        ),
        format_metric(
            "Average Score",
            no_rerank_metrics["avg_score"],
            rerank_metrics["avg_score"],
            False,
        ),
        format_metric(
            "Average Text",
            no_rerank_metrics["avg_text"],
            rerank_metrics["avg_text"],
            False,
        ),
        format_metric(
            "Average Code",
            no_rerank_metrics["avg_code"],
            rerank_metrics["avg_code"],
            False,
        ),
    ]

    if no_rerank_metrics["errors"] or rerank_metrics["errors"]:
        metrics.append(
            format_metric(
                "Errors", no_rerank_metrics["errors"], rerank_metrics["errors"]
            )
        )

    panel = Panel("\n\n".join(metrics), title="Metrics", border_style="cyan")
    console.print(panel)
