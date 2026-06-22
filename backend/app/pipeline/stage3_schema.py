from typing import Dict, Any
from app.schemas.app_config import AppConfig
from app.engine.llm_client import get_llm_client

def generate_schema(design: Dict[str, Any]) -> AppConfig:
    client = get_llm_client()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        response_model=AppConfig,
        messages=[
            {"role": "system", "content": "Convert the design into a structured AppConfig with UI, API, DB, and Auth configuration."},
            {"role": "user", "content": f"Design: {design}"}
        ]
    )
    return response