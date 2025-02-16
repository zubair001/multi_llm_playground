from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.db import crud
from app.api.routes import router as llm_router
from app.models.request_models import PromptRequest
from app.services.llm_services import process_llm_query
from app.db.models import User, Model

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/")
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    return crud.create_user(db, name, email)

@app.post("/models/")
def create_model(name: str, version: str, db: Session = Depends(get_db)):
    return crud.create_model(db, name, version)

@app.post("/responses/")
def save_response(user_id: int, model_id: int, query: str, response: str, db: Session = Depends(get_db)):
    return crud.save_response(db, user_id, model_id, query, response)

@app.post("/ask/")
async def ask_llm(request: PromptRequest, db: Session = Depends(get_db)):
    # Use a default user_id (e.g., 1) for now
    user_id = 1

    # Retrieve user from the database (optional for now if you want to use a default user)
    user = db.query(User).filter_by(id=user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Ensure that we have a valid model ID or create one if it doesn't exist
    model = db.query(Model).filter_by(name=request.model).first()
    if not model:
        # You can either create a model if not found or return an error
        model = crud.create_model(db, name=request.model, version="latest")

    # Process LLM query and save response
    response = await process_llm_query(db, user_id, request.text, model.id, request.model)

    return response

# Include additional routes
app.include_router(llm_router)
