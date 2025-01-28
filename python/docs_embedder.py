import asyncio
import argparse
import uuid
import httpx
from pathlib import Path
from qdrant_client import QdrantClient
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
from loguru import logger
from tqdm import tqdm
from rich.console import Console
from rich.table import Table
from rich import box
from rich.markdown import Markdown
from rich.panel import Panel
from utils import generate_embeddings, chunk_markdown, situate_context, rerank
from config import COLLECTION_NAME, EMBEDDING_DIM, QUERY_PROMPT
from typing import List, Dict, Optional, Union, Any
from smolagents import Tool
import re


class LLMContentTool(Tool):
    name = "llm_content_tool"
    description = "A tool that fetches main documentation content from operator-ui.vercel.app/llms.txt"
    inputs = {}  # No inputs needed since URL is fixed
    output_type = "string"

    def forward(self) -> Any:
        """Fetch the documentation content from the fixed URL."""
        try:
            response = httpx.get("https://operator-ui.vercel.app/llms.txt")
            response.raise_for_status()
            return response.text
        except httpx.HTTPError as e:
            raise RuntimeError(f"Failed to fetch docs content: {str(e)}")


class DocsSearchTool(Tool):
    name = "docs_search_tool"
    description = "A tool that searches through Diffusion Studio's documentation to find relevant code examples and syntax."
    inputs = {
        "query": {
            "type": "string",
            "description": "The search query about DiffStudio's functionality (e.g. 'how to add text overlay' or 'video transitions')",
        },
        "limit": {
            "type": "integer",
            "description": "Maximum number of results to return",
            "nullable": True,
        },
        "filter_conditions": {
            "type": "object",
            "description": "Optional filters for specific documentation sections",
            "nullable": True,
        },
        "rerank_results": {
            "type": "boolean",
            "description": "Whether to use semantic reranking for more accurate results",
            "nullable": True,
        },
    }
    output_type = "array"

    def forward(
        self,
        query: str,
        limit: int = 5,
        filter_conditions: Optional[
            Dict[str, Union[str, int, float, List[str]]]
        ] = None,
        rerank_results: bool = False,
    ) -> Any:
        """Search for documentation snippets."""
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            # If no loop is running, create a new one
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            try:
                return loop.run_until_complete(
                    self._async_forward(query, limit, filter_conditions, rerank_results)
                )
            finally:
                loop.close()
        else:
            # If we're already in an event loop, just create the coroutine
            return loop.create_task(
                self._async_forward(query, limit, filter_conditions, rerank_results)
            )

    async def _async_forward(
        self,
        query: str,
        limit: int,
        filter_conditions: Optional[Dict[str, Union[str, int, float, List[str]]]],
        rerank_results: bool,
    ) -> List[Dict]:
        """Async implementation of the forward method."""
        return await search_docs(
            query=query,
            limit=limit,
            filter_conditions=filter_conditions,
            rerank_results=rerank_results,
        )


async def search_docs(
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
        client = QdrantClient(path="docs/vector_db")
        logger.debug("Connected to vector DB")

        # Generate embedding for query
        query_embedding = await generate_embeddings(QUERY_PROMPT + query)
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
            collection_name=COLLECTION_NAME,
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
            # Take top K results for reranking
            top_k = min(5, len(hits))
            docs_to_rerank = [hit["content"] for hit in hits[:top_k] if hit["content"]]
            logger.info(f"Reranking top {top_k} results...")
            logger.debug(f"Reranking {len(docs_to_rerank)} documents")

            rerank_scores = await rerank(query=query, documents=docs_to_rerank)
            logger.debug(f"Got {len(rerank_scores)} rerank scores")
            logger.debug(
                f"Sample rerank result: {rerank_scores[0] if rerank_scores else None}"
            )

            # Combine vector similarity and rerank scores (70-30 split) for top K
            for hit, rerank_result in zip(hits[:top_k], rerank_scores):
                rerank_dict = (
                    rerank_result[0]
                    if isinstance(rerank_result, list)
                    else rerank_result
                )
                rerank_score = float(rerank_dict.get("score", 0.0))
                old_score = hit["score"]
                hit["score"] = 0.7 * old_score + 0.3 * rerank_score
                logger.debug(
                    f"Combined scores for {hit['filepath']}: "
                    f"vector={old_score:.3f}, rerank={rerank_score:.3f}, "
                    f"final={hit['score']:.3f}"
                )

            # Sort all results, keeping non-reranked scores for results after top K
            hits = sorted(hits, key=lambda x: x["score"], reverse=True)

        # Return requested number of results
        return hits[:limit]

    except Exception as e:
        logger.error(f"Failed to search docs: {str(e)}")
        raise


async def embed_docs(debug: bool = False):
    try:
        # Initialize Qdrant client with persistent storage
        client = QdrantClient(path="docs/vector_db")
        logger.info("Connected to Qdrant DB")

        # Create collection if it doesn't exist
        try:
            client.get_collection(COLLECTION_NAME)
        except (
            ValueError,
            KeyError,
        ):  # Qdrant raises these when collection doesn't exist
            client.create_collection(
                collection_name=COLLECTION_NAME,
                vectors_config=VectorParams(
                    size=EMBEDDING_DIM, distance=Distance.COSINE
                ),
            )
            logger.info(f"Created new collection: {COLLECTION_NAME}")
        else:
            logger.info(f"Using existing collection: {COLLECTION_NAME}")

        # Get all MD files recursively including subdirectories
        docs_dir = Path(__file__).parent.parent / "docs"
        md_files = []
        for pattern in ["*.md", "*/*.md", "*/*/*.md"]:
            md_files.extend(docs_dir.glob(pattern))
        md_files = sorted(set(md_files))

        if debug:
            md_files = md_files[:5]
            logger.warning("DEBUG MODE: Processing only first 5 files")

        logger.info(
            f"Found {len(md_files)} markdown files in {docs_dir} and subdirectories"
        )

        # Collect all points for batch upload
        points = []
        for md_file in tqdm(md_files, desc="Processing files", unit="file"):
            try:
                full_content = md_file.read_text(encoding="utf-8")
                chunks = chunk_markdown(full_content)
                logger.info(f"Processing {md_file.name} in {len(chunks)} chunks")

                for i, chunk in enumerate(
                    tqdm(
                        chunks,
                        desc=f"Chunks of {md_file.name}",
                        unit="chunk",
                        leave=False,
                    )
                ):
                    try:
                        # Generate context for the chunk
                        contextialzed_chunk, usage = await situate_context(
                            full_content, chunk
                        )
                        logger.debug(f"Context generation usage: {usage} for chunk {i}")

                        # Generate embedding for the chunk
                        text_to_embed = f"{chunk}\n\n{contextialzed_chunk}"
                        embedding = await generate_embeddings(text_to_embed)

                        if len(embedding) != EMBEDDING_DIM:
                            raise ValueError(
                                f"Expected embedding dimension {EMBEDDING_DIM}, got {len(embedding)}"
                            )

                        # Create point for the chunk
                        rel_path = md_file.relative_to(docs_dir)
                        readable_id = (
                            f"{rel_path}#chunk{i}" if len(chunks) > 1 else str(rel_path)
                        )

                        points.append(
                            PointStruct(
                                id=str(uuid.uuid4()),
                                vector=embedding,
                                payload={
                                    "file_id": readable_id,
                                    "filename": md_file.name,
                                    "filepath": str(rel_path),
                                    "chunk_index": i,
                                    "total_chunks": len(chunks),
                                    "original_content": chunk,
                                    "contextualized_content": contextialzed_chunk,
                                },
                            )
                        )
                        logger.debug(
                            f"Processed embedding for chunk {i + 1}/{len(chunks)}"
                        )

                        # Upload points in small batches to avoid memory issues
                        if len(points) >= 32:
                            try:
                                logger.info(
                                    f"Uploading batch of {len(points)} points to Qdrant..."
                                )
                                client.upload_points(
                                    collection_name=COLLECTION_NAME,
                                    points=points,
                                    batch_size=32,
                                )
                                points = []
                                logger.debug("Batch upload complete")
                            except Exception as e:
                                logger.error(f"Failed to upload batch: {str(e)}")
                                # Continue processing but keep points in memory
                                continue

                    except Exception as e:
                        logger.error(
                            f"Failed to process chunk {i} of {md_file.name}: {str(e)}"
                        )
                        continue

            except Exception as e:
                logger.error(f"Failed to process file {md_file.name}: {str(e)}")
                continue

        # Upload any remaining points
        if points:
            try:
                logger.info(f"Uploading final {len(points)} points to Qdrant...")
                client.upload_points(
                    collection_name=COLLECTION_NAME,
                    points=points,
                    batch_size=32,
                )
                logger.success(f"Successfully uploaded final {len(points)} chunks")
            except Exception as e:
                logger.error(f"Failed to upload final batch: {str(e)}")
                raise

        logger.success("Completed embedding all documents")

    except Exception as e:
        logger.exception(f"Failed to embed docs: {str(e)}")
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


async def evaluate_search(
    query: str, reference_file: str, reference_answer: str, use_rerank: bool = False
) -> Dict:
    """Evaluate search results for a single query against reference."""
    results = await search_docs(query=query, limit=5, rerank_results=use_rerank)

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
                    rerank_result1 = await rerank(
                        query=ref_text, documents=[found_text]
                    )
                    text_scores.append(
                        float(rerank_result1[0][0]["score"]) if rerank_result1 else 0
                    )
                    # Found -> Reference
                    rerank_result2 = await rerank(
                        query=found_text, documents=[ref_text]
                    )
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
                        rerank_result1 = await rerank(
                            query=ref_code, documents=[found_code]
                        )
                        code_scores.append(
                            float(rerank_result1[0][0]["score"])
                            if rerank_result1
                            else 0
                        )
                        # Found -> Reference
                        rerank_result2 = await rerank(
                            query=found_code, documents=[ref_code]
                        )
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


async def run_evaluation():
    """Run evaluation on all QnA pairs in docs/qna directory."""
    qna_dir = Path(__file__).parent.parent / "docs" / "qna"
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
                    metrics_no_rerank = await evaluate_search(
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
                    metrics_with_rerank = await evaluate_search(
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


async def main():
    parser = argparse.ArgumentParser(description="Embed and search documentation")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Embed command
    embed_parser = subparsers.add_parser("embed", help="Embed documentation")
    embed_parser.add_argument(
        "--debug", action="store_true", help="Process only first 5 files"
    )

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

    subparsers.add_parser("eval", help="Evaluate search on QnA pairs")

    args = parser.parse_args()

    if args.command == "embed":
        await embed_docs(debug=args.debug)
    elif args.command == "search":
        filter_conditions = {}
        if args.filepath:
            filter_conditions["filepath"] = args.filepath
        if args.chunk_index is not None:
            filter_conditions["chunk_index"] = args.chunk_index

        results = await search_docs(
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
        table.add_column("Score", justify="right", width=4)
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

            # Show section info (e.g., "Part 1/3")
            section_info = (
                f"Part {hit['chunk_index'] + 1}/{hit['total_chunks']}"
                if hit["chunk_index"] is not None and hit["total_chunks"] > 1
                else "Full Doc"
            )

            table.add_row(
                str(i), f"{hit['score']:.3f}", hit["filepath"], section_info, content_md
            )

        console.print("\n")
        console.print(table)
        console.print("\n")
    elif args.command == "eval":
        await run_evaluation()


if __name__ == "__main__":
    logger.add("docs_embedder.log", rotation="100 MB")
    asyncio.run(main())
