# Universal AI Chat (Multi-Provider Router)

- CLI:
  python main.py chat "hello world" -m openai

- API:
  uvicorn api:app --reload --port 8000
  curl -X POST http://127.0.0.1:8000/chat \
    -H "Content-Type: application/json" \
    -d '{"prompt":"explain RLHF","model":"deepseek"}'

Environment:
- copy .env.example to .env and set keys.
- If a key is missing, the service returns a harmless mock string.

Providers:
- services/openai_service.py
- services/gemini_service.py
- services/deepseek_service.py

Router:
- router.ask_ai(model, prompt)
