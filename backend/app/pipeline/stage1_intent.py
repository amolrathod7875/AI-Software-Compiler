from app.schemas.user_intent import IntentModel
from app.engine.llm_client import get_llm_client

def extract_intent(prompt: str) -> IntentModel:
    client = get_llm_client()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        response_model=IntentModel,
        messages=[
            {"role": "system", "content": "Extract entities, actions, relationships, and constraints from the user prompt. Be specific and thorough."},
            {"role": "user", "content": prompt}
        ]
    )
    return response