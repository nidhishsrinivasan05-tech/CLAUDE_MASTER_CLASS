from fastapi import FastAPI
from .routers import auth, tasks

app = FastAPI(title="FastAPI Auth App")

app.include_router(auth.router)
app.include_router(tasks.router)

@app.get("/health")
def health():
    return {"status": "ok"}
