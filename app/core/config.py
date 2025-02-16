import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    YOUR_SITE_URL = os.getenv("YOUR_SITE_URL")
    YOUR_SITE_NAME = os.getenv("YOUR_SITE_NAME")
    DEFAULT_MODEL = os.getenv("DEFAULT_MODEL")
    BASE_URL = os.getenv("BASE_URL")
    DATABASE_URL = os.getenv("DATABASE_URL")


    @staticmethod
    def validate():
        """Ensures required environment variables are set."""
        if not Config.OPENROUTER_API_KEY:
            raise ValueError("Missing API_KEY in .env")
        if not Config.YOUR_SITE_URL:
            raise ValueError("Missing YOUR_SITE_URL in .env")
        if not Config.YOUR_SITE_NAME:
            raise ValueError("Missing YOUR_SITE_NAME in .env")
        if not Config.DEFAULT_MODEL:
            raise ValueError("Missing DEFAULT_MODEL in .env")
        if not Config.BASE_URL:
            raise ValueError("Missing BASE_URL in .env")

# Validate configuration at startup
Config.validate()
