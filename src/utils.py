import os
import httpx
import re
import time
import argparse
import uuid
import hashlib
import unicodedata
import ftfy

from loguru import logger
from pathlib import Path
from typing import List, Dict, Optional, Union
from rich.console import Console
from rich.panel import Panel
from qdrant_client import QdrantClient

from src.prompts import QUERY_PROMPT
from src.settings import settings


from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct,
    Filter,
    FieldCondition,
    Range,
    MatchText,
    MatchAny,
    ScoredPoint,
)
from tqdm import tqdm
from rich.table import Table
from rich import box
from rich.markdown import Markdown

client = QdrantClient(path=settings.qdrant_path)
logger.info("Connected to Qdrant DB")


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


def generate_embeddings(
    text: str | list[str], timeout=30, retries=settings.max_retries
) -> list[list[float]]:
    """
    Generate embeddings for the given text using Infinity API (synchronous version).

    Args:
        text (str | list[str]): Text or list of texts to embed
        timeout (int, optional): Request timeout in seconds. Defaults to 30.
        retries (int, optional): Number of retries on failure. Defaults to MAX_RETRIES.

    Returns:
        list[list[float]]: List of embeddings for each input text
    """
    from openai import OpenAI

    client = OpenAI(
        api_key=settings.infinity_api_key, base_url=settings.infinity_base_url
    )
    last_error = None

    for attempt in range(retries):
        try:
            logger.debug(
                f"Making embedding request with {len(text) if isinstance(text, list) else 1} texts"
            )
            response = client.embeddings.create(
                model=settings.infinity_embedding_model,
                input=text if isinstance(text, list) else [text],
            )
            embeddings = [data.embedding for data in response.data]
            logger.debug("Got embeddings successfully")
            return embeddings

        except Exception as e:
            last_error = e
            logger.warning(f"Error during embedding attempt {attempt + 1}: {str(e)}")

            if attempt < retries - 1:
                delay = settings.retry_delay * (attempt + 1)  # Exponential backoff
                logger.warning(
                    f"Embedding attempt {attempt + 1} failed. Retrying in {delay}s..."
                )
                time.sleep(delay)
                continue

    error_msg = f"Request failed after {retries} attempts"
    raise RuntimeError(f"{error_msg}: {str(last_error)}")


def rerank(query: str, documents: list[str], timeout=30, retries=settings.max_retries):
    """
    Rerank documents based on relevance to query using Infinity reranking API (synchronous version).

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
            with httpx.Client() as client:
                response = client.post(
                    f"{settings.infinity_base_url}/rerank",
                    json={
                        "model": settings.infinity_rerank_model,
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
            delay = settings.retry_delay * (attempt + 1)  # Exponential backoff
            logger.warning(
                f"Reranking attempt {attempt + 1} failed. Retrying in {delay}s..."
            )
            time.sleep(delay)
            continue

    error_msg = f"Rerank request failed after {retries} attempts"
    if isinstance(last_error, httpx.TimeoutException):
        raise TimeoutError(f"{error_msg}: Timeout - {str(last_error)}")
    elif isinstance(last_error, httpx.RequestError):
        raise RuntimeError(f"{error_msg}: Request failed - {str(last_error)}")
    else:
        raise RuntimeError(f"{error_msg}: {str(last_error)}")


def search_docs(
    query: str,
    limit: int = 5,
    filter_conditions: Optional[Dict[str, Union[str, int, float, List[str]]]] = None,
    rerank_results: bool = False,
) -> List[Dict]:
    """
    A tool that searches through Diffusion Studio's documentation to find relevant code examples and syntax.
    It helps you find the right way to use DiffStudio's video editing library.
    """
    try:
        logger.info(f"Starting search for query: '{query}'")
        logger.debug("Connected to vector DB")

        # Generate embedding for query
        query_embeddings = generate_embeddings(QUERY_PROMPT + query)
        query_embedding = query_embeddings[0]  # Take first embedding
        logger.debug(f"Generated query embedding of size {len(query_embedding)}")

        # Build filter if conditions provided
        search_filter = None
        if filter_conditions:
            logger.info(f"Applying filters: {filter_conditions}")
            must_conditions = []
            for field, value in filter_conditions.items():
                if isinstance(value, (int, float)):
                    must_conditions.append(
                        FieldCondition(key=field, range=Range(gte=value))
                    )
                elif isinstance(value, str):
                    must_conditions.append(
                        FieldCondition(key=field, match=MatchText(text=value))
                    )
                elif isinstance(value, list):
                    must_conditions.append(
                        FieldCondition(key=field, match=MatchAny(any=value))
                    )

            if must_conditions:
                search_filter = Filter(must=must_conditions)
                logger.debug(f"Created filter with {len(must_conditions)} conditions")

        # Get initial results from vector search
        vector_limit = limit * 3 if rerank_results else limit
        logger.info(
            f"Fetching top {vector_limit} results{' for reranking' if rerank_results else ''}"
        )
        search_results = client.query_points(
            collection_name=settings.collection_name,
            query=query_embedding,
            query_filter=search_filter,
            limit=vector_limit,
        )

        # Format initial results
        hits = []
        if search_results and hasattr(search_results, "points"):
            points = search_results.points
            logger.info(f"Found {len(points)} initial matches")
        else:
            points = []
            logger.warning("No initial matches found")

        for point in points:
            if not isinstance(point, ScoredPoint):
                logger.warning(f"Skipping result with unexpected type: {type(point)}")
                continue

            payload = point.payload or {}
            hits.append(
                {
                    "score": float(point.score),
                    "content": payload.get("original_content"),
                    "context": payload.get("contextualized_content"),
                    "filepath": payload.get("filepath"),
                    "chunk_index": payload.get("chunk_index"),
                    "total_chunks": payload.get("total_chunks"),
                }
            )
            logger.debug(
                f"Added hit from {payload.get('filepath')} with score {point.score:.3f}"
            )

        if hits and rerank_results:
            # Rerank all results instead of just top 5
            docs_to_rerank = [hit["content"] for hit in hits if hit["content"]]
            logger.info(f"Reranking {len(docs_to_rerank)} results...")
            logger.debug(f"Reranking {len(docs_to_rerank)} documents")

            rerank_scores = rerank(query=query, documents=docs_to_rerank)
            logger.debug(f"Got {len(rerank_scores)} rerank scores")

            logger.debug(
                f"Sample rerank result: {rerank_scores[0] if rerank_scores else None}"
            )

            # Keep vector and rerank scores separate
            for hit, rerank_result in zip(hits, rerank_scores):
                rerank_dict = (
                    rerank_result[0]
                    if isinstance(rerank_result, list)
                    else rerank_result
                )
                hit["vector_score"] = hit["score"]  # Store original vector score
                hit["rerank_score"] = float(
                    rerank_dict.get("score", 0.0)
                )  # Store rerank score
                # Use rerank score as primary score when reranking
                hit["score"] = hit["rerank_score"]
                logger.debug(
                    f"Scores for {hit['filepath']}: "
                    f"vector={hit['vector_score']:.3f}, rerank={hit['rerank_score']:.3f}"
                )

            # Sort by rerank score
            hits = sorted(hits, key=lambda x: x["score"], reverse=True)

        # Return requested number of results
        return hits[:limit]

    except Exception as e:
        logger.error(f"Failed to search docs: {str(e)}")
        raise


def ensure_collection_exists():
    """Ensure collection exists and is properly configured."""
    try:
        # Create collection if it doesn't exist
        try:
            client.get_collection(settings.collection_name)
            logger.info(f"Using existing collection: {settings.collection_name}")
        except (ValueError, KeyError):
            client.create_collection(
                collection_name=settings.collection_name,
                vectors_config=VectorParams(
                    size=settings.embedding_dim, distance=Distance.COSINE
                ),
            )
            logger.info(f"Created new collection: {settings.collection_name}")

        return client
    except Exception as e:
        logger.error(f"Failed to setup collection: {str(e)}")
        raise


def fetch_and_hash_content(url: str) -> tuple[str, str]:
    """Fetch content and generate its hash."""
    with httpx.Client() as client:
        response = client.get(url)
        response.raise_for_status()
        # Fix text encoding issues
        content = ftfy.fix_text(response.content.decode("utf-8", errors="replace"))
        # Normalize unicode characters
        content = unicodedata.normalize("NFKC", content)
        # Generate hash of normalized content
        content_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()
        return content, content_hash


def upload_points_batch(points: List[PointStruct]):
    """Upload a batch of points to Qdrant."""
    try:
        logger.info(f"Uploading batch of {len(points)} points...")
        client.upload_points(
            collection_name=settings.collection_name,
            points=points,
            batch_size=32,
        )
        logger.debug("Batch upload complete")
    except Exception as e:
        logger.error(f"Failed to upload batch: {str(e)}")
        raise


def auto_embed_pipeline(
    url: str,
    hash_file: str = "docs/content_hash.txt",
    debug: bool = False,
    force: bool = False,
):
    """Automated pipeline to fetch, check hash, and embed content if changed."""
    try:
        logger.info(
            f"Starting auto-embed pipeline for {url}{' (DEBUG MODE)' if debug else ''}{' (FORCE UPDATE)' if force else ''}"
        )

        # Ensure collection exists
        ensure_collection_exists()

        # Fetch content and generate hash
        content, new_hash = fetch_and_hash_content(url)
        logger.info(f"Generated hash: {new_hash}")

        # Initialize hash path
        hash_path = Path(hash_file)

        # Check if hash exists and has changed (skip if force)
        if not force:
            has_existing_hash = hash_path.exists()

            # Check if we have embeddings for this URL
            has_embeddings = False
            try:
                results = client.query_points(
                    collection_name=settings.collection_name,
                    query_filter=Filter(
                        must=[FieldCondition(key="source", match=MatchText(text=url))]
                    ),
                    limit=1,
                )
                has_embeddings = bool(results and results.points)
                logger.info(f"Found existing embeddings: {has_embeddings}")
            except Exception as e:
                logger.warning(f"Failed to check existing embeddings: {str(e)}")

            # Only skip if we have both matching hash and embeddings
            if has_existing_hash and has_embeddings:
                old_hash = hash_path.read_text().strip()
                if old_hash == new_hash:
                    logger.info("Content unchanged and embeddings exist, skipping")
                    return
                logger.info(
                    f"Content changed (old hash: {old_hash[:8]}..., new hash: {new_hash[:8]}...)"
                )
            else:
                if not has_existing_hash:
                    logger.info("No previous hash found")
                if not has_embeddings:
                    logger.info("No embeddings found for URL")
                logger.info("Processing as new content")
        else:
            logger.info("Force update requested, processing content")

        # Store new hash immediately
        hash_path.parent.mkdir(parents=True, exist_ok=True)
        hash_path.write_text(new_hash)
        logger.info("Stored new content hash")

        # Content is new or changed
        logger.info("Processing chunks...")

        # Clear existing URL content if any
        try:
            client.delete(
                collection_name=settings.collection_name,
                points_selector=Filter(
                    must=[FieldCondition(key="source", match=MatchText(text=url))]
                ),
            )
            logger.info(f"Cleared existing content for {url}")
        except Exception as e:
            logger.warning(f"Failed to clear existing content: {str(e)}")

        # Split content into chunks by separator
        chunks = split_by_separator(content)
        if debug:
            chunks = chunks[:5]  # Take only first 5 chunks in debug mode
            logger.info(f"Debug mode: processing first 5/{len(chunks)} chunks")
        else:
            logger.info(f"Split content into {len(chunks)} chunks")

        # Process chunks in batches
        batch_size = 32
        points = []
        chunks_to_embed = []
        chunk_metadata = []  # Store metadata for each chunk

        for i, chunk in enumerate(tqdm(chunks, desc="Processing chunks")):
            try:
                # Extract filename from chunk if present
                chunk_lines = chunk.split("\n")
                filename = None
                if chunk_lines[0].startswith("File:"):
                    filename = chunk_lines[0].replace("File:", "").strip()
                    chunk = "\n".join(chunk_lines[1:]).strip()

                # Store chunk and metadata for batch processing
                chunks_to_embed.append(chunk)
                chunk_metadata.append(
                    {"index": i, "filename": filename or url, "chunk": chunk}
                )

                # Process batch when full
                if len(chunks_to_embed) >= batch_size:
                    # Generate embeddings for batch
                    embeddings = generate_embeddings(chunks_to_embed)

                    # Create points from embeddings and metadata
                    for emb, meta in zip(embeddings, chunk_metadata):
                        points.append(
                            PointStruct(
                                id=str(uuid.uuid4()),
                                vector=emb,
                                payload={
                                    "file_id": f"url_content#{meta['index']}",
                                    "filename": meta["filename"],
                                    "filepath": meta["filename"],
                                    "source": url,
                                    "chunk_index": meta["index"],
                                    "total_chunks": len(chunks),
                                    "original_content": meta["chunk"],
                                },
                            )
                        )

                    # Upload batch
                    upload_points_batch(points)

                    # Clear batches
                    chunks_to_embed = []
                    chunk_metadata = []
                    points = []

            except Exception as e:
                logger.error(f"Failed to process chunk {i}: {str(e)}")
                continue

        # Process remaining chunks
        if chunks_to_embed:
            try:
                # Generate embeddings for remaining chunks
                embeddings = generate_embeddings(chunks_to_embed)

                # Create points from embeddings and metadata
                for emb, meta in zip(embeddings, chunk_metadata):
                    points.append(
                        PointStruct(
                            id=str(uuid.uuid4()),
                            vector=emb,
                            payload={
                                "file_id": f"url_content#{meta['index']}",
                                "filename": meta["filename"],
                                "filepath": meta["filename"],
                                "source": url,
                                "chunk_index": meta["index"],
                                "total_chunks": len(chunks),
                                "original_content": meta["chunk"],
                            },
                        )
                    )

                # Upload remaining batch
                if points:
                    upload_points_batch(points)
            except Exception as e:
                logger.error(f"Failed to process final batch: {str(e)}")

        logger.success("Successfully updated content and embeddings")

    except Exception as e:
        logger.exception(f"Auto-embed pipeline failed: {str(e)}")
        raise


def split_by_separator(content: str, separator: str = "---") -> list[str]:
    """Split content by separator and clean chunks."""
    # Fix any encoding issues and normalize
    content = (
        ftfy.fix_text(content)
        if isinstance(content, str)
        else ftfy.fix_text(content.decode("utf-8", errors="replace"))
    )
    content = unicodedata.normalize("NFKC", content)

    chunks = []
    raw_chunks = [chunk.strip() for chunk in content.split(separator) if chunk.strip()]

    for chunk in raw_chunks:
        lines = chunk.split("\n")
        # Skip empty chunks
        if not lines:
            continue

        # Find the filename line (format: # filename.md)
        filename = None
        content_lines = []
        in_content = False

        for line in lines:
            if not filename and line.startswith("# ") and ".md" in line:
                # Extract filename from the markdown header (e.g. "# 0-welcome.md" -> "0-welcome.md")
                filename = line.replace("#", "").strip()
                in_content = True
                continue

            if in_content:
                content_lines.append(line)

        if filename and content_lines:
            content = "\n".join(content_lines).strip()
            if content:  # Only add if there's content
                chunks.append(f"File: {filename}\n\n{content}")

    return chunks


def evaluate_search(
    query: str, reference_file: str, reference_answer: str, use_rerank: bool = False
) -> Dict:
    """Evaluate search results for a single query against reference."""
    # Get more results for reranking
    vector_limit = 15 if use_rerank else 5
    results = search_docs(query=query, limit=vector_limit, rerank_results=use_rerank)

    # Take top 5 after reranking if needed
    results = results[:5]

    # Normalize reference path
    reference_file = normalize_path(reference_file)

    # Get referenced file from results with normalized paths
    found_reference = any(
        normalize_path(hit["filepath"]) == reference_file for hit in results
    )

    # Calculate metrics
    metrics = {
        "reference_found": found_reference,
        "reference_rank": -1,
        "top_score": results[0]["score"] if results else 0,
        "semantic_match": False,
        "semantic_score": 0.0,
        "code_match": False,
        "code_score": 0.0,
        "found_content": None,
    }

    # Find rank of reference if present
    for i, hit in enumerate(results):
        if normalize_path(hit["filepath"]) == reference_file:
            metrics["reference_rank"] = i + 1
            metrics["found_content"] = hit["content"]

            # Check if content semantically matches reference answer
            if hit["content"]:
                # Extract code blocks
                ref_code_match = re.search(
                    r"```(?:javascript)?\n(.*?)\n```", reference_answer, re.DOTALL
                )
                found_code_match = re.search(
                    r"```(?:javascript)?\n(.*?)\n```", hit["content"], re.DOTALL
                )

                # Get text without code blocks
                ref_text = re.sub(
                    r"```(?:javascript)?\n.*?\n```",
                    "",
                    reference_answer,
                    flags=re.DOTALL,
                ).strip()
                found_text = re.sub(
                    r"```(?:javascript)?\n.*?\n```", "", hit["content"], flags=re.DOTALL
                ).strip()

                # Calculate text similarity (bi-directional)
                if ref_text and found_text:
                    text_scores = []
                    # Reference -> Found
                    rerank_result1 = rerank(query=ref_text, documents=[found_text])
                    text_scores.append(
                        float(rerank_result1[0][0]["score"]) if rerank_result1 else 0
                    )

                    # Found -> Reference
                    rerank_result2 = rerank(query=found_text, documents=[ref_text])
                    text_scores.append(
                        float(rerank_result2[0][0]["score"]) if rerank_result2 else 0
                    )

                    # Take average of bi-directional scores
                    metrics["semantic_score"] = sum(text_scores) / len(text_scores)
                    metrics["semantic_match"] = metrics["semantic_score"] > 0.7

                # Calculate code similarity if code blocks exist
                if ref_code_match and found_code_match:
                    ref_code = normalize_code(ref_code_match.group(1))
                    found_code = normalize_code(found_code_match.group(1))

                    if ref_code and found_code:
                        code_scores = []
                        # Reference -> Found
                        rerank_result1 = rerank(query=ref_code, documents=[found_code])

                        code_scores.append(
                            float(rerank_result1[0][0]["score"])
                            if rerank_result1
                            else 0
                        )
                        # Found -> Reference
                        rerank_result2 = rerank(query=found_code, documents=[ref_code])
                        code_scores.append(
                            float(rerank_result2[0][0]["score"])
                            if rerank_result2
                            else 0
                        )
                        # Take average of bi-directional scores
                        metrics["code_score"] = sum(code_scores) / len(code_scores)
                        metrics["code_match"] = (
                            metrics["code_score"] > 0.8
                        )  # Higher threshold for code
            break

    return metrics


def run_evaluation():
    """Run evaluation on all QnA pairs in docs/evals/embeddings directory."""
    qna_dir = Path(__file__).parent.parent / "docs" / "evals" / "embeddings"
    results_no_rerank = []
    results_with_rerank = []

    # Get all QnA pairs first
    qna_paths = sorted(qna_dir.glob("[0-9]*"))
    total_pairs = len(qna_paths)

    logger.info(f"Found {total_pairs} QnA pairs to evaluate")

    # Process each QnA directory with progress bar
    with tqdm(total=total_pairs * 2, desc="Evaluating", unit="searches") as pbar:
        for qna_path in qna_paths:
            try:
                # Load QnA files
                question = (qna_path / "question.txt").read_text().strip()
                reference = (qna_path / "reference.txt").read_text().strip().split("\n")
                answer = (qna_path / "answer.txt").read_text()

                # Get reference file and lines
                ref_file = reference[0]
                ref_lines = (
                    f"{reference[1]} - {reference[2]}" if len(reference) > 2 else ""
                )

                base_result = {
                    "id": qna_path.name,
                    "question": question,
                    "reference": ref_file,
                    "reference_lines": ref_lines,
                    "reference_answer": answer,  # Add reference answer to results
                }

                # Vector search only
                try:
                    pbar.set_description(f"Vector search for Q{qna_path.name}")
                    metrics_no_rerank = evaluate_search(
                        question, ref_file, answer, use_rerank=False
                    )
                    results_no_rerank.append({**base_result, **metrics_no_rerank})
                except Exception as e:
                    logger.error(f"Vector search failed for {qna_path.name}: {str(e)}")
                    results_no_rerank.append(
                        {
                            **base_result,
                            "reference_found": False,
                            "reference_rank": -1,
                            "top_score": 0,
                            "error": str(e),
                        }
                    )
                pbar.update(1)

                # With reranking
                try:
                    pbar.set_description(f"Reranking for Q{qna_path.name}")
                    metrics_with_rerank = evaluate_search(
                        question, ref_file, answer, use_rerank=True
                    )
                    results_with_rerank.append({**base_result, **metrics_with_rerank})
                except Exception as e:
                    logger.error(f"Reranking failed for {qna_path.name}: {str(e)}")
                    results_with_rerank.append(
                        {
                            **base_result,
                            "reference_found": False,
                            "reference_rank": -1,
                            "top_score": 0,
                            "error": str(e),
                        }
                    )
                pbar.update(1)

            except Exception as e:
                logger.error(f"Failed to process {qna_path.name}: {str(e)}")
                error_result = {
                    "id": qna_path.name,
                    "question": "ERROR",
                    "reference": "ERROR",
                    "reference_lines": "",
                    "reference_answer": "",
                    "reference_found": False,
                    "reference_rank": -1,
                    "top_score": 0,
                    "error": str(e),
                }
                results_no_rerank.append(error_result)
                results_with_rerank.append(error_result)
                pbar.update(2)
                continue

    # Print results and comparison
    no_rerank_metrics = print_results(
        "Vector Search Results (No Reranking)", results_no_rerank
    )
    rerank_metrics = print_results(
        "Vector Search Results (With Reranking)", results_with_rerank
    )
    print_comparison(no_rerank_metrics, rerank_metrics)


def main():
    parser = argparse.ArgumentParser(description="Search and manage documentation")

    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Search command
    search_parser = subparsers.add_parser("search", help="Search documentation")
    search_parser.add_argument("query", help="Search query")
    search_parser.add_argument("--limit", type=int, default=5, help="Number of results")
    search_parser.add_argument("--filepath", help="Filter by filepath")
    search_parser.add_argument("--chunk-index", type=int, help="Filter by chunk index")
    search_parser.add_argument(
        "--rerank",
        action="store_true",
        help="Apply semantic reranking (slower but more accurate)",
    )
    search_parser.add_argument(
        "--full-content",
        action="store_true",
        help="Show full content instead of truncated version",
    )

    # Evaluation command
    subparsers.add_parser("eval", help="Evaluate search on QnA pairs")

    # Auto-embed command
    auto_embed_parser = subparsers.add_parser("auto-embed", help="Auto-embed from URL")
    auto_embed_parser.add_argument(
        "--url",
        default=f"{settings.url}/llms.txt",
        help="URL to fetch content from",
    )
    auto_embed_parser.add_argument(
        "--hash-file",
        default="docs/content_hash.txt",
        help="File to store content hash",
    )
    auto_embed_parser.add_argument(
        "--debug", action="store_true", help="Debug mode - process only first 5 chunks"
    )
    auto_embed_parser.add_argument(
        "--force",
        action="store_true",
        help="Force update embeddings even if content unchanged",
    )

    args = parser.parse_args()

    if args.command == "auto-embed":
        auto_embed_pipeline(args.url, args.hash_file, args.debug, args.force)
    elif args.command == "search":
        filter_conditions = {}
        if args.filepath:
            filter_conditions["filepath"] = args.filepath
        if args.chunk_index is not None:
            filter_conditions["chunk_index"] = args.chunk_index

        results = search_docs(
            query=args.query,
            limit=args.limit,
            filter_conditions=filter_conditions if filter_conditions else None,
            rerank_results=args.rerank,
        )

        console = Console()
        table = Table(
            show_header=True,
            header_style="bold magenta",
            box=box.ROUNDED,
            title=f"[bold cyan]Search Results for: [yellow]'{args.query}'[/yellow] ({len(results)} hits)[/bold cyan]",
            show_lines=True,
        )

        table.add_column("#", style="dim", width=4)
        table.add_column("Vector", justify="right", width=6)
        table.add_column("Rerank", justify="right", width=6) if args.rerank else None
        table.add_column("File", style="green", width=4)
        table.add_column("Section", justify="center", width=4)
        table.add_column("Content", ratio=1, no_wrap=args.full_content)

        for i, hit in enumerate(results, 1):
            content = hit["content"] or "N/A"
            if not args.full_content:
                content = content[:200] + "..." if len(content) > 200 else content

            # Format content as markdown with code highlighting
            content_md = Markdown(
                content, code_theme="monokai", inline_code_theme="monokai"
            )

            # Add context if available
            if hit["context"] and args.full_content:
                context_md = Markdown(
                    f"\n**Context:**\n{hit['context']}",
                    code_theme="monokai",
                    inline_code_theme="monokai",
                )
                content_md = f"{content_md}\n{context_md}"

            # Show section info
            section_info = (
                f"Part {hit['chunk_index'] + 1}/{hit['total_chunks']}"
                if hit["chunk_index"] is not None and hit["total_chunks"] > 1
                else "Full Doc"
            )

            # Add row with both scores if reranking
            if args.rerank:
                table.add_row(
                    str(i),
                    f"{hit.get('vector_score', 0):.3f}",
                    f"{hit.get('rerank_score', 0):.3f}",
                    hit["filepath"],
                    section_info,
                    content_md,
                )
            else:
                table.add_row(
                    str(i),
                    f"{hit['score']:.3f}",
                    hit["filepath"],
                    section_info,
                    content_md,
                )

        console.print("\n")
        console.print(table)
        console.print("\n")
    elif args.command == "eval":
        run_evaluation()


if __name__ == "__main__":
    logger.add("embedding_pipeline.log", rotation="100 MB")
    main()
