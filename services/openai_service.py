from utils.config import OPENAI_API_KEY
from utils.logger import log

# Replace this placeholder with the real OpenAI client calls
def query(prompt: str) -> str:
    if not OPENAI_API_KEY:
        return "[openai:mock] You asked: " + prompt
    # TODO: implement real API call
    log("Calling OpenAI with real key...")
    return "OpenAI response placeholder for: " + prompt
