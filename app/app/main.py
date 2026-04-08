from fastapi import FastAPI

app = FastAPI(
    title="Mental Health AI Agent",
    description="Agente de apoio emocional e bem-estar mental (não clínico).",
    version="0.1.0",
)


@app.get("/health")
def health():
    return {"status": "ok"}
