from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.llm_services import process_llm_query
from app.db.models import User
from app.models.request_models import PromptRequest

router = APIRouter()

@router.post("/ask/")
async def ask_llm(request: PromptRequest, db: Session = Depends(get_db)):
    """
    API endpoint to send a query to LLM and store the response.
    """
    # Check if user exists
    user = db.query(User).filter_by(id=request.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return await process_llm_query(db, request.user_id, request.text, request.model, "latest")
