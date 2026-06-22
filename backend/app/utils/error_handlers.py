from typing import Any, Dict
from app.schemas.user_intent import IntentModel

def handle_vague_prompt(prompt: str) -> IntentModel:
    intent = IntentModel(
        entities=[],
        actions=[],
        relationships=[],
        constraints=[],
        assumptions=[f"Input was vague - '{prompt}' lacks specific entities or actions"]
    )
    return intent

def handle_conflicting_reqs(reqs: Dict[str, Any]) -> Dict[str, Any]:
    return {"resolved": reqs}