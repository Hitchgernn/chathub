from utils.config import OPENAI_API_KEY
from utils.logger import log
from openai import OpenAI

def query(prompt: str) -> str:
    if not OPENAI_API_KEY:
        return "[openai:mock] You asked: " + prompt

    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # or "gpt-4-turbo", "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": prompt},
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        log(f"[openai error] {e}")
        return f"[openai:error] {e}"