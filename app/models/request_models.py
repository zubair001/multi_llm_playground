from pydantic import BaseModel
import os
from app.core.config import Config


class PromptRequest(BaseModel):
    text: str
    user_id: int
    model: str = Config.DEFAULT_MODEL