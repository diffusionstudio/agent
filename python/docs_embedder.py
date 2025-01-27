import asyncio
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
from utils import generate_embeddings, chunk_markdown, situate_context
from config import COLLECTION_NAME, EMBEDDING_DIM
from typing import List, Dict, Optional, Union, cast


async def search_docs(
    query: str,
    limit: int = 5,
    filter_conditions: Optional[Dict[str, Union[str, int, float, List[str]]]] = None,
) -> List[Dict]:
    """
    Search for similar documents using a text query.

    Args:
        query: Text query to search for
        limit: Number of results to return
        filter_conditions: Optional dict of field conditions for filtering
            Example: {"filepath": "api/classes/", "chunk_index": 0}

    Returns:
        List of matching documents with scores and metadata
    """
    try:
        client = QdrantClient(path="docs/vector_db")

        # Generate embedding for query
        query_embedding = await generate_embeddings(query)

        # Build filter if conditions provided
        search_filter = None
        if filter_conditions:
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

        # Execute search
        results = client.query_points(
            collection_name=COLLECTION_NAME,
            query=query_embedding,
            query_filter=search_filter,
            limit=limit,
        )

        # Format results
        hits = []
        for scored_point in cast(List[ScoredPoint], results):
            payload = scored_point.payload or {}
            hits.append(
                {
                    "score": scored_point.score,
                    "content": payload.get("original_content"),
                    "context": payload.get("contextualized_content"),
                    "filepath": payload.get("filepath"),
                    "chunk_index": payload.get("chunk_index"),
                    "total_chunks": payload.get("total_chunks"),
                }
            )

        return hits

    except Exception as e:
        logger.exception(f"Failed to search docs: {str(e)}")
        raise


async def embed_docs():
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
        logger.info(
            f"Found {len(md_files)} markdown files in {docs_dir} and subdirectories"
        )

        # Main progress bar for files
        for md_file in tqdm(md_files, desc="Processing files", unit="file"):
            try:
                full_content = md_file.read_text(encoding="utf-8")
                chunks = chunk_markdown(full_content)
                logger.info(f"Processing {md_file.name} in {len(chunks)} chunks")

                points = []
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
                        chunk_id = (
                            f"{rel_path}#chunk{i}" if len(chunks) > 1 else str(rel_path)
                        )

                        points.append(
                            PointStruct(
                                id=chunk_id,
                                vector=embedding,
                                payload={
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

                # Batch upsert points for this file
                if points:
                    client.upsert(collection_name=COLLECTION_NAME, points=points)
                    logger.success(f"Embedded {len(points)} chunks from {md_file.name}")

            except Exception as e:
                logger.error(f"Failed to process file {md_file.name}: {str(e)}")
                continue

        logger.success("Completed embedding all documents")

    except Exception as e:
        logger.exception(f"Failed to embed docs: {str(e)}")
        raise


if __name__ == "__main__":
    logger.add("docs_embedder.log", rotation="100 MB")
    asyncio.run(embed_docs())
