from __future__ import annotations

import weaviate
from weaviate.classes.init import AdditionalConfig, Auth

from coursemind.config import load_settings


def connect():
    """
    Connect to Weaviate Cloud using env vars.
    """
    s = load_settings()

    headers = {
        # Query/Transformation/Personalization Agents need an inference provider key.
        # The official docs show passing provider keys via headers; we keep it generic.
        "X-Inference-Api-Key": s.inference_api_key,
        "X-Inference-Provider": s.inference_provider,
    }

    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=s.weaviate_url,
        auth_credentials=Auth.api_key(s.weaviate_api_key),
        additional_config=AdditionalConfig(headers=headers),
    )

    return client

