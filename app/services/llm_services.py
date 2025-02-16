from sqlalchemy.orm import Session
from datetime import datetime
from app.db.models import Query, Response, Model
from app.core.openrouter_client import client
from app.core.config import Config

async def call_llm(model_name: str, prompt: str) -> str:
    """
    Sends a request to an LLM API and returns the response.
    """
    try:
        completion = client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": prompt}],
            extra_headers={
                "HTTP-Referer": Config.YOUR_SITE_URL,
                "X-Title": Config.YOUR_SITE_NAME,
            },
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

async def process_llm_query(db: Session, user_id: int, question: str, model_name: str, model_version: str):
    """
    Saves the query in the database, sends it to the LLM, and stores the response.
    """
    # Ensure the model exists in the database
    model = db.query(Model).filter_by(name=model_name, version=model_version).first()
    if not model:
        model = Model(name=model_name, version=model_version)
        db.add(model)
        db.commit()
        db.refresh(model)

    # Save the query
    query = Query(user_id=user_id, question=question, timestamp=datetime.utcnow())
    db.add(query)
    db.commit()
    db.refresh(query)

    # Get response from LLM
    response_text = await call_llm(model_name, question)

    # Save response in DB
    response = Response(
        user_id=user_id,
        model_id=model.id,
        query_id=query.id,
        response_text=response_text,
        created_at=datetime.utcnow()
    )
    db.add(response)
    db.commit()

    return {"query": question, "response": response_text}
