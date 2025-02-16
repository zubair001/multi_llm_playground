from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from typing import AsyncGenerator
from app.core.openrouter_client import client
from app.core.config import Config
from app.models.request_models import PromptRequest

router = APIRouter()

async def generate_streaming_response(prompt: str, model: str) -> AsyncGenerator[str, None]:
    """Streaming response generator for async LLM responses."""
    try:
        stream = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            stream=True,
            extra_headers={
                "HTTP-Referer": Config.YOUR_SITE_URL,
                "X-Title": Config.YOUR_SITE_NAME,
            },
        )
        async for chunk in stream:
            yield chunk.choices[0].delta.content or ""

    except Exception as e:
        yield f"Error: {str(e)}"

@router.post("/generate")
async def generate_text(request: PromptRequest):
    """Generates text using the selected LLM."""
    try:
        completion = client.chat.completions.create(
            model=request.model,
            messages=[{"role": "user", "content": request.text}],
            extra_headers={
                "HTTP-Referer": Config.YOUR_SITE_URL,
                "X-Title": Config.YOUR_SITE_NAME,
            },
        )
        return {"response": completion.choices[0].message.content}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/generate-stream")
async def generate_streaming_text(request: PromptRequest):
    """Generates text using the selected LLM and returns a streaming response."""
    return StreamingResponse(generate_streaming_response(request.text, request.model), media_type="text/plain")
