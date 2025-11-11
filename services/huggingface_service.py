import os
from utils.config import HUGGINGFACE_API_KEY
from utils.logger import log
from huggingface_hub import InferenceClient

def query(prompt: str) -> str:
    if not HUGGINGFACE_API_KEY:
        return "[huggingface:mock] You asked: " + prompt

    try:
        client = InferenceClient(api_key=HUGGINGFACE_API_KEY)
        response = client.chat.completions.create(
            model="mistralai/Mixtral-8x7B-Instruct-v0.1",  # replace with whichever model you want
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        log(f"[huggingface error] {e}")
        return f"[huggingface:error] {e}"
