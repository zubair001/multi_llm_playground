from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    queries = relationship("Query", back_populates="user", cascade="all, delete-orphan")  # ✅ Fix
    responses = relationship("Response", back_populates="user", cascade="all, delete-orphan")

class Query(Base):
    __tablename__ = "queries"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    question = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    responses = relationship("Response", back_populates="query", cascade="all, delete-orphan")
    user = relationship("User", back_populates="queries")

class Model(Base):
    __tablename__ = "models"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    version = Column(String, nullable=False)

    responses = relationship("Response", back_populates="model", cascade="all, delete-orphan")

class Response(Base):
    __tablename__ = "responses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    model_id = Column(Integer, ForeignKey("models.id", ondelete="CASCADE"), nullable=False)
    query_id = Column(Integer, ForeignKey("queries.id", ondelete="CASCADE"), nullable=False)  # ✅ Fix
    response_text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="responses")
    model = relationship("Model", back_populates="responses")
    query = relationship("Query", back_populates="responses")
