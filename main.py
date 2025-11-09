import typer
from utils.logger import log
from router import ask_ai
from utils.config import MODEL_FALLBACK

app = typer.Typer(add_completion=False)

@app.command()
def chat(prompt: str, model: str = typer.Option(MODEL_FALLBACK, "--model", "-m")):
    """
    Example:
      python main.py chat "hello" -m gemini
    """
    try:
        resp = ask_ai(model, prompt)
        log(f"[{model}] {resp}")
    except Exception as e:
        log(f"[error] {e}")
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()
