from typing import Any, Dict, List
from app.schemas.app_config import AppConfig, APIConfig, DBConfig, UIConfig, AuthConfig
from app.engine.llm_client import get_llm_client

def auto_repair(data: Dict[str, Any]) -> AppConfig:
    repaired = {
        "ui": UIConfig() if "ui" not in data else UIConfig(**data["ui"]),
        "api": APIConfig() if "api" not in data else APIConfig(**data["api"]),
        "db": DBConfig() if "db" not in data else DBConfig(**data["db"]),
        "auth": AuthConfig() if "auth" not in data else AuthConfig(**data["auth"])
    }
    return AppConfig(**repaired)

def regenerate_failed_parts(error_loc: List[Any]) -> Dict[str, Any]:
    client = get_llm_client()
    error_path = ".".join(str(x) for x in error_loc)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        response_model=Dict[str, Any],
        messages=[
            {"role": "system", "content": "Generate valid configuration data for the failed path."},
            {"role": "user", "content": f"Fix the schema error at: {error_path}"}
        ]
    )
    return response