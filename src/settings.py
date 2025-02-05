import os
from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    embedding_dim: int = 1024
    infinity_base_url: str = "https://muhtasham--infinity-serve.modal.run"
    infinity_api_key: str = Field(default="sk-dummy")
    infinity_embedding_model: str = "mixedbread-ai/mxbai-embed-large-v1"
    infinity_rerank_model: str = "mixedbread-ai/mxbai-rerank-base-v1"
    url: str = "https://operator.diffusion.studio"  # or: change to http://localhost:5173
    hash_file: str = "docs/content_hash.txt"

    qdrant_path: str = "embeddings/vector_db"
    collection_name: str = "diffusion_studio_docs"

    anthropic_api_key: str = Field(
        default_factory=lambda: os.getenv("ANTHROPIC_API_KEY", "")
    )
    playwright_chromium_executable_path: Optional[str] = Field(
        default_factory=lambda: os.getenv("PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH")
    )
    playwright_web_socket_url: Optional[str] = Field(
        default_factory=lambda: os.getenv("PLAYWRIGHT_WEB_SOCKET_URL")
    )

    max_retries: int = 10
    retry_delay: int = Field(default=10, description="Retry delay in seconds")

    class Config:
        env_prefix = ""
        case_sensitive = False


settings = Settings()
