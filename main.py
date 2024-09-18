from datetime import datetime

from fastapi import FastAPI

from app.api.v1.router import router as api_router

app = FastAPI()


@app.get("/ping")
def ping():
    return {"now": datetime.now()}


app.include_router(api_router, prefix="/api/v1")
