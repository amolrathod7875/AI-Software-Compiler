from typing import Any, Dict, List
from pydantic import ValidationError
from app.schemas.app_config import AppConfig

def validate_config(data: Dict[str, Any]) -> tuple[bool, List[str]]:
    errors = []
    try:
        AppConfig.model_validate(data)
        return True, []
    except ValidationError as e:
        for err in e.errors():
            errors.append(f"{'.'.join(str(x) for x in err['loc'])}: {err['msg']}")
        return False, errors

def detect_invalid_json(data: Any) -> bool:
    if not isinstance(data, dict):
        return True
    return False

def check_missing_keys(data: Dict[str, Any], required_keys: List[str]) -> List[str]:
    missing = []
    for key in required_keys:
        if key not in data:
            missing.append(key)
    return missing

def check_mismatches(data: Dict[str, Any], schema: Any) -> List[Any]:
    try:
        schema.model_validate(data)
        return []
    except ValidationError as e:
        return [err["loc"] for err in e.errors()]