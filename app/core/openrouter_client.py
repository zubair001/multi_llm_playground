from openai import OpenAI
from app.core.config import Config
import os

# Initialize OpenAI client for OpenRouter
client = OpenAI(
    base_url=Config.BASE_URL,
    api_key=Config.OPENROUTER_API_KEY,
)
