from app.db.session import engine
from app.db.base import Base
from app.db.models import User, Model, Response  # Ensure all models are imported

# Create tables
Base.metadata.create_all(bind=engine)

print("Database tables created successfully!")
