from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="AI Software Compiler API")
app.include_router(router, prefix="/api")