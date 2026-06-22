import os
from openai import OpenAI
import instructor

def get_llm_client():
    api_key = os.getenv("LLM_API_KEY", "test-key")
    client = instructor.from_openai(OpenAI(api_key=api_key))
    return client

def structured_prompt(prompt: str, schema_hint: str) -> str:
    return f"{prompt}\n\nSchema hint: {schema_hint}"