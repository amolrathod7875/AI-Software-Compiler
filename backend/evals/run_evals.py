import json
from app.pipeline.stage1_intent import extract_intent
from app.pipeline.stage2_design import generate_design
from app.pipeline.stage3_schema import generate_schema
from app.pipeline.stage4_refinement import refine_config
from app.evals.metrics_tracker import MetricsTracker

metrics = MetricsTracker()

def run_real_prompts():
    with open("evals/datasets/real_prompts.json") as f:
        prompts = json.load(f)
    results = []
    for p in prompts:
        try:
            intent = extract_intent(p["prompt"])
            design = generate_design(intent)
            schema = generate_schema(design)
            config = refine_config(schema)
            results.append({"prompt": p["prompt"], "success": True, "config": config})
        except Exception as e:
            results.append({"prompt": p["prompt"], "success": False, "error": str(e)})
    return results

def run_edge_cases():
    with open("evals/datasets/edge_cases.json") as f:
        prompts = json.load(f)
    results = []
    for p in prompts:
        try:
            result = extract_intent(p["prompt"])
            results.append({"prompt": p["prompt"], "success": False, "error": "Should have failed for vague input"})
        except Exception as e:
            results.append({"prompt": p["prompt"], "success": True, "handled": True})
    return results