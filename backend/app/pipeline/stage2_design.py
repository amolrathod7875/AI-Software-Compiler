from typing import List, Dict, Any
from app.schemas.user_intent import IntentModel
from app.engine.llm_client import get_llm_client

def generate_design(intent: IntentModel) -> Dict[str, Any]:
    client = get_llm_client()
    prompt = f"Entities: {intent.entities}\nActions: {intent.actions}\nRelationships: {intent.relationships}\nConstraints: {intent.constraints}"
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        response_model=Dict[str, Any],
        messages=[
            {"role": "system", "content": "Generate a software design with entities, flows, roles, and UI components based on the extracted intent."},
            {"role": "user", "content": prompt}
        ]
    )
    return response