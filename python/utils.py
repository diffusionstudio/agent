import os
import httpx
from config import MXBAI_API_URL, MXBAI_HEADERS

async def generate_embeddings(payload, timeout=30):
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

def clear_file_path(output: str):
    """Clears the output path if it exists."""
    if os.path.exists(output):
        os.remove(output)
        print(f"Removed existing file: {output}")