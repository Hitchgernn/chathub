import os
from dotenv import load_dotenv

# Make absolutely sure .env loads as soon as this module is imported
load_dotenv(override=True)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
MODEL_FALLBACK = os.getenv("MODEL_FALLBACK", "openai")