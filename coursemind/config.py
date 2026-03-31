from __future__ import annotations

from dataclasses import dataclass
import os

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
    weaviate_url: str
    weaviate_api_key: str
    inference_provider: str
    inference_api_key: str
    visible_collections: tuple[str, ...]


def load_settings() -> Settings:
    load_dotenv()

    weaviate_url = os.getenv("WEAVIATE_URL", "").strip()
    weaviate_api_key = os.getenv("WEAVIATE_API_KEY", "").strip()
    inference_provider = os.getenv("INFERENCE_PROVIDER", "openai").strip()
    inference_api_key = os.getenv("INFERENCE_API_KEY", "").strip()

    visible = os.getenv("COURSEMIND_VISIBLE_COLLECTIONS", "Courses,Instructors").strip()
    visible_collections = tuple([x.strip() for x in visible.split(",") if x.strip()])

    missing = []
    if not weaviate_url:
        missing.append("WEAVIATE_URL")
    if not weaviate_api_key:
        missing.append("WEAVIATE_API_KEY")
    if not inference_api_key:
        missing.append("INFERENCE_API_KEY")

    if missing:
        raise RuntimeError(
            "Missing required environment variables: " + ", ".join(missing) + ". "
            "Copy .env.example to .env and fill in the values."
        )

    return Settings(
        weaviate_url=weaviate_url,
        weaviate_api_key=weaviate_api_key,
        inference_provider=inference_provider,
        inference_api_key=inference_api_key,
        visible_collections=visible_collections,
    )

