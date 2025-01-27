import asyncio
from pathlib import Path
import vecs
from loguru import logger
from tqdm import tqdm
from utils import generate_embeddings, chunk_markdown, situate_context
from config import DB_CONNECTION

if not DB_CONNECTION:
    raise ValueError("DB_CONNECTION must be set in config.py")

async def embed_docs():
    try:
        # Initialize vecs client
        vx = vecs.create_client(DB_CONNECTION)
        logger.info("Connected to vector DB")
        
        # Create or get collection for docs
        docs = vx.get_or_create_collection(name="docs", dimension=1024)
        logger.info("Created/got docs collection")
        
        # Get all MD files
        docs_dir = Path(__file__).parent.parent / "docs"
        md_files = list(docs_dir.glob("**/*.md"))
        logger.info(f"Found {len(md_files)} markdown files")
        
        # Main progress bar for files
        for md_file in tqdm(md_files, desc="Processing files", unit="file"):
            try:
                # Read full content first
                full_content = md_file.read_text(encoding='utf-8')
                chunks = chunk_markdown(full_content)
                logger.info(f"Processing {md_file.name} in {len(chunks)} chunks")
                
                # Nested progress bar for chunks
                chunk_pbar = tqdm(total=len(chunks), desc=f"Chunks of {md_file.name}", unit="chunk", leave=False)
                for i, chunk in enumerate(chunks):
                    try:
                        # Generate embedding for chunk
                        embedding = await generate_embeddings(chunk)
                        
                        # Get context for chunk
                        context, usage = await situate_context(full_content, chunk)
                        logger.debug(f"Context generation usage: {usage} for chunk {i}")
                        
                        # Each chunk gets its own record with unique ID
                        chunk_id = f"{md_file}#chunk{i}" if len(chunks) > 1 else str(md_file)
                        
                        # Store in vector DB
                        docs.upsert(
                            records=[
                                (
                                    chunk_id,
                                    embedding[0],  # First embedding from response
                                    {
                                        "filename": md_file.name,
                                        "chunk_index": i,
                                        "total_chunks": len(chunks),
                                        "content": chunk,
                                        "context": context
                                    }
                                )
                            ]
                        )
                        logger.success(f"Embedded {md_file.name} chunk {i+1}/{len(chunks)}")
                        chunk_pbar.update(1)
                    except Exception as e:
                        logger.error(f"Failed to process chunk {i} of {md_file.name}: {str(e)}")
                        continue
                chunk_pbar.close()
            except Exception as e:
                logger.error(f"Failed to process file {md_file.name}: {str(e)}")
                continue
        
        # Create index for faster queries
        docs.create_index()
        logger.success("Created vector index")
        
        # Cleanup
        vx.disconnect()
        logger.info("Disconnected from vector DB")
        
    except Exception as e:
        logger.exception(f"Failed to embed docs: {str(e)}")
        raise

if __name__ == "__main__":
    logger.add("docs_embedder.log", rotation="100 MB")
    asyncio.run(embed_docs()) 