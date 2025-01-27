import asyncio
from pathlib import Path
import argparse
import uuid
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
from utils import generate_embeddings, chunk_markdown, situate_context, rerank
from config import COLLECTION_NAME, EMBEDDING_DIM
from typing import List, Dict, Optional, Union


async def search_docs(
    query: str,
    limit: int = 5,
    filter_conditions: Optional[Dict[str, Union[str, int, float, List[str]]]] = None,
    rerank_results: bool = False,
) -> List[Dict]:
    """
    Search for similar documents using a text query.

    Args:
        query: Text query to search for
        limit: Number of results to return
        filter_conditions: Optional dict of field conditions for filtering
            Example: {"filepath": "api/classes/", "chunk_index": 0}
        rerank_results: Whether to apply semantic reranking (slower but more accurate)

    Returns:
        List of matching documents with scores and metadata
    """
    try:
        logger.info(f"Starting search for query: '{query}'")
        client = QdrantClient(path="docs/vector_db")
        logger.debug("Connected to vector DB")

        # Generate embedding for query
        query_embedding = await generate_embeddings(query)
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

        # Get results (more if we're going to rerank)
        vector_limit = min(limit * 3, 20) if rerank_results else limit
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
            # Rerank results
            logger.info("Reranking results...")
            docs_to_rerank = [hit["content"] for hit in hits if hit["content"]]
            logger.debug(f"Reranking {len(docs_to_rerank)} documents")

            rerank_scores = await rerank(query=query, documents=docs_to_rerank)
            logger.debug(f"Got {len(rerank_scores)} rerank scores")
            logger.debug(
                f"Sample rerank result: {rerank_scores[0] if rerank_scores else None}"
            )

            # Combine vector similarity and rerank scores (70-30 split)
            for hit, rerank_result in zip(hits, rerank_scores):
                # Each rerank result is a list of dictionaries, take first one's score
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

            # Sort by combined score and limit results
            hits = sorted(hits, key=lambda x: x["score"], reverse=True)[:limit]
            logger.info(f"Returning top {len(hits)} results after reranking")
        else:
            # Just take top N results from vector search
            hits = hits[:limit]
            logger.info(f"Returning top {len(hits)} results from vector search")

        return hits

    except Exception as e:
        logger.exception(f"Failed to search docs: {str(e)}")
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
                        contextialzed_chunk, usage = await situate_context(
                            full_content, chunk
                        )
                        logger.debug(f"Context generation usage: {usage} for chunk {i}")

                        text_to_embed = f"{chunk}\n\n{contextialzed_chunk}"
                        embedding = await generate_embeddings(text_to_embed)

                        if len(embedding) != EMBEDDING_DIM:
                            raise ValueError(
                                f"Expected embedding dimension {EMBEDDING_DIM}, got {len(embedding)}"
                            )

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
                            f"Prepared chunk {i + 1}/{len(chunks)} for embedding"
                        )

                    except Exception as e:
                        logger.error(
                            f"Failed to process chunk {i} of {md_file.name}: {str(e)}"
                        )
                        continue

            except Exception as e:
                logger.error(f"Failed to process file {md_file.name}: {str(e)}")
                continue

        # Batch upload all points
        if points:
            logger.info(f"Uploading {len(points)} points to Qdrant...")
            client.upload_points(
                collection_name=COLLECTION_NAME,
                points=points,
                batch_size=64,  # Adjust based on your memory constraints
            )
            logger.success(f"Successfully uploaded {len(points)} chunks")

        logger.success("Completed embedding all documents")

    except Exception as e:
        logger.exception(f"Failed to embed docs: {str(e)}")
        raise


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


if __name__ == "__main__":
    logger.add("docs_embedder.log", rotation="100 MB")
    asyncio.run(main())
