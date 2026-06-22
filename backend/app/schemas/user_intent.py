from typing import List, Optional
from pydantic import BaseModel, model_validator

class IntentModel(BaseModel):
    entities: List[str] = []
    actions: List[str] = []
    relationships: List[str] = []
    constraints: List[str] = []
    assumptions: List[str] = []

    @model_validator(mode='after')
    def check_vague_input(self):
        if not self.entities and not self.actions:
            self.assumptions.append("Input was vague - no entities or actions detected")
        return self