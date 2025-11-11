import requests
from utils.config import HUGGINGFACE_API_KEY
from utils.logger import log

HUGGINGFACE_MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.2"
API_URL = f"https://api-inference.huggingface.co/models/{HUGGINGFACE_MODEL_NAME}"

def query(prompt: str) -> str:
    if not HUGGINGFACE_API_KEY:
        return "[huggingface:mock] You asked: " + prompt

    try:
        headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
        # Format the prompt according to Mistral's instruction format
        formatted_prompt = f"<s>[INST] {prompt} [/INST]"
        payload = {"inputs": formatted_prompt}
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raise an exception for bad status codes
        result = response.json()
        # The response from this model is a list with a single dictionary
        return result[0]['generated_text']
    except Exception as e:
        log(f"[huggingface error] {e}")
        # Check if the response body is available and log it for more context
        if 'response' in locals() and hasattr(response, 'text'):
            log(f"Response body: {response.text}")
        return f"[huggingface:error] {e}"