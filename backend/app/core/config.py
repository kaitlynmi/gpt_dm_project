from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Config:
    ZHIPU_GLM_API_KEY = os.getenv("ZHIPU_GLM_API_KEY")
    ZHIPU_API_BASE_URL = os.getenv("ZHIPU_API_BASE_URL")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///dev.db")

config = Config()