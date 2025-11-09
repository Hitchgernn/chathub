from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from router import ask_ai
from utils.logger import log
from utils.config import MODEL_FALLBACK

class ChatIn(BaseModel):
    prompt: str
    model: str | None = None

class ChatOut(BaseModel):
    model: str
    response: str

app = FastAPI(title="Universal AI Chat")

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/chat", response_model=ChatOut)
def chat(inbody: ChatIn):
    model = inbody.model or MODEL_FALLBACK
    try:
        resp = ask_ai(model, inbody.prompt)
        return ChatOut(model=model, response=resp)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        log(f"[server-error] {e}")
        raise HTTPException(status_code=500, detail="Internal error")
