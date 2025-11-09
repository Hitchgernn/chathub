import requests
from utils.config import DEEPSEEK_API_KEY
from utils.logger import log

def query(prompt: str) -> str:
    if not DEEPSEEK_API_KEY:
        return "[deepseek:mock] You asked: " + prompt

    try:
        url = "https://api.deepseek.com/chat/completions"
        headers = {
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()

        return result["choices"][0]["message"]["content"]

    except Exception as e:
        log(f"[deepseek error] {e}")
        return f"[deepseek:error] {e}"
