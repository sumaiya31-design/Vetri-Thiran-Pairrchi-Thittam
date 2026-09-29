import os

from dotenv import load_dotenv

load_dotenv()


APP_NAME = os.getenv("APP_NAME", "EduGenie")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

MAX_INPUT_CHARS = int(os.getenv("MAX_INPUT_CHARS", "30000"))
REQUEST_TIMEOUT_SECONDS = int(
    os.getenv("REQUEST_TIMEOUT_SECONDS", "60")
)