from fastapi import FastAPI
from datetime import datetime
from app.api.v1.api import router as api_router

app = FastAPI()

@app.get("/ping")
def ping():
    return { "now": datetime.now() }

app.include_router(api_router, prefix="/api/v1")