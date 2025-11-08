from services import gemini_service, openai_service, deepseek_service

def ask_ai(model: str, prompt: str) -> str:
    model = (model or "").lower()
    if model in ("openai", "gpt", "gpt-4", "gpt-3.5"):
        return openai_service.query(prompt)
    if model in ("gemini", "google", "veo"):
        return gemini_service.query(prompt)
    if model in ("deepseek",):
        return deepseek_service.query(prompt)
    raise ValueError(f"Unsupported model: {model}")
