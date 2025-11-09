import typer
from utils.logger import log
from router import ask_ai
from utils.config import MODEL_FALLBACK

def main(model: str = typer.Option(MODEL_FALLBACK, "--model", "-m"),
         prompt: str = typer.Argument(...)):
    """
    Example:
      python main.py -m gemini "Explain AI in one sentence"
    """
    try:
        resp = ask_ai(model, prompt)
        log(f"[{model}] {resp}")
    except Exception as e:
        log(f"[error] {e}")
        raise typer.Exit(code=1)

if __name__ == "__main__":
    typer.run(main)