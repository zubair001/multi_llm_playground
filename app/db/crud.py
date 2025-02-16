from sqlalchemy.orm import Session
from .models import User, Query, Model, Response

def create_user(db: Session, name: str, email: str):
    new_user = User(name=name, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_or_create_model(db: Session, name: str, version: str = None):
    """Check if the model exists, otherwise create it."""
    model = db.query(Model).filter(Model.name == name, Model.version == version).first()
    if not model:
        model = Model(name=name, version=version)
        db.add(model)
        db.commit()
        db.refresh(model)
    return model

def save_query_response(db: Session, user_id: int, question: str, model_name: str, model_version: str, response_text: str):
    """Save the user query and model response."""
    query = Query(user_id=user_id, question=question)
    db.add(query)
    db.commit()
    db.refresh(query)

    model = get_or_create_model(db, model_name, model_version)

    response = Response(query_id=query.id, model_id=model.id, response_text=response_text)
    db.add(response)
    db.commit()
    db.refresh(response)

    return response

def get_responses_for_user(db: Session, user_id: int):
    """Get all responses for a user, including the model info."""
    return db.query(Query).filter(Query.user_id == user_id).all()