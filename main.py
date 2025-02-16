from fastapi import FastAPI
from app.api.v1.endpoints import chat

#Initialize FastAPI app
app = FastAPI(
    title="Multi-LLM API with Streaming",
    version="1.0",
    description="A FastAPI backend supporting multiple LLMs with streaming.",
)

#Include routes
app.include_router(chat.router, prefix="/api/v1", tags=["LLM Chat"])

#Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the Multi-LLM API!"}
