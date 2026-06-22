from typing import Any, Dict

def simulate(config: Dict[str, Any]) -> bool:
    required_stages = ["ui", "api", "db", "auth"]
    for stage in required_stages:
        if stage not in config:
            return False
    return True