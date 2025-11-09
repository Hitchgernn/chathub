from utils.config import GEMINI_API_KEY
from utils.logger import log
import google.genai as genai

def query(prompt: str) -> str:
    if not GEMINI_API_KEY:
        return "[gemini:mock] You asked: " + prompt

    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
        response = client.models.generate_content(
            model="models/gemini-flash-latest",
            config = genai.types.GenerateContentConfig(
                system_instruction="You are a rude teacher"
            ),
            contents=prompt
        )
        return response.text
    except Exception as e:
        log(f"[gemini error] {e}")
        return f"[gemini:error] {e}"