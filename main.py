from fastapi import FastAPI
from app.api.v1.api import router as api_router

from datetime import datetime

app = FastAPI()

@app.get("/ping")
def ping():
    return { "now": datetime.now() }

app.include_router(api_router, prefix="/api/v1")