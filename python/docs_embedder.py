import asyncio
from pathlib import Path
import vecs
from utils import generate_embeddings
from config import DB_CONNECTION

if not DB_CONNECTION:
    raise ValueError("DB_CONNECTION must be set in config.py")

async def embed_docs():
    # Initialize vecs client
    vx = vecs.create_client(DB_CONNECTION)
    
    # Create or get collection for docs
    docs = vx.get_or_create_collection(name="docs", dimension=1024)  # Using MXBAI dimension
    
    # Get all MD files
    docs_dir = Path(__file__).parent.parent / "docs"
    md_files = list(docs_dir.glob("**/*.md"))
    
    for md_file in md_files:
        # Read file content
        content = md_file.read_text(encoding='utf-8')
        
        # Generate embedding
        embedding = await generate_embeddings({
            "text": content,
            "model": "mixedbread-ai/mxbai-embed-large-v1"
        })
        
        # Store in vector DB
        docs.upsert(
            records=[
                (
                    str(md_file),  # Use filepath as ID
                    embedding['data'][0]['embedding'],  # The embedding vector
                    {
                        "filename": md_file.name,
                        "content": content
                    }
                )
            ]
        )
        print(f"Embedded {md_file.name}")
    
    # Create index for faster queries
    docs.create_index()
    
    # Cleanup
    vx.disconnect()

if __name__ == "__main__":
    asyncio.run(embed_docs()) 