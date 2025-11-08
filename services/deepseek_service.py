from utils.config import DEEPSEEK_API_KEY
from utils.logger import log

def query(prompt: str) -> str:
    if not DEEPSEEK_API_KEY:
        return "[deepseek:mock] You asked: " + prompt
    # TODO: implement real API call
    log("Calling DeepSeek with real key...")
    return "DeepSeek response placeholder for: " + prompt
