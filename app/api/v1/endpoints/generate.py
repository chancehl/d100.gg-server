from fastapi import APIRouter

router = APIRouter()

@router.get("/generate/")
def generate_list(q: str):
    return {"q": q}