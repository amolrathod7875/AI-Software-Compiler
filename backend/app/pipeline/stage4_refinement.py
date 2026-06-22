from app.schemas.app_config import AppConfig
from app.engine.validator import validate_config
from app.engine.llm_client import get_llm_client

def refine_config(config: AppConfig) -> dict:
    is_valid, errors = validate_config(config.model_dump())
    if is_valid:
        return config.model_dump()
    
    client = get_llm_client()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        response_model=AppConfig,
        messages=[
            {"role": "system", "content": "Fix the validation errors in the configuration."},
            {"role": "user", "content": f"Config: {config.model_dump()}\nErrors: {errors}"}
        ]
    )
    return response.model_dump()