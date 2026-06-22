from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.pipeline.stage1_intent import extract_intent
from app.pipeline.stage2_design import generate_design
from app.pipeline.stage3_schema import generate_schema
from app.pipeline.stage4_refinement import refine_config
from evals.metrics_tracker import MetricsTracker
import time

router = APIRouter()
metrics = MetricsTracker()

class PromptRequest(BaseModel):
    prompt: str

@router.post("/generate")
async def generate_config(request: PromptRequest):
    start_time = time.time()
    try:
        intent = extract_intent(request.prompt)
        design = generate_design(intent)
        schema = generate_schema(design)
        config = refine_config(schema)
        latency = time.time() - start_time
        metrics.record(success=True, latency=latency)
        return {"config": config, "metrics": {"latency": latency, "success_rate": metrics.success_rate}}
    except Exception as e:
        latency = time.time() - start_time
        metrics.record(success=False, latency=latency)
        raise HTTPException(status_code=500, detail=str(e))