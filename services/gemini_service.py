from utils.config import GEMINI_API_KEY
from utils.logger import log

def query(prompt: str) -> str:
    if not GEMINI_API_KEY:
        return "[gemini:mock] You asked: " + prompt
    # TODO: implement real API call
    log("Calling Gemini with real key...")
    return "Gemini response placeholder for: " + prompt
