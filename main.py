from fastapi import FastAPI, Form
from src.graph import run_graph
from src.state import DetailedLevel, TargetAudience

app = FastAPI()


@app.post("/explain")
def explain(
    message: str = Form(...),
    audience: TargetAudience = Form(...),
    detail: DetailedLevel = Form(...),
):
    return run_graph(message, audience, detail)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
