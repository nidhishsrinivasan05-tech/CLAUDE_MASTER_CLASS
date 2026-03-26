from fastapi import FastAPI

app = FastAPI(title="Fullstack Starter Backend")

@app.get("/health")
def health():
    return {"status": "ok", "message": "Connect your frontend here"}
