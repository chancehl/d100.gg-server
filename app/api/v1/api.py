from fastapi import APIRouter

from .endpoints import generate

router = APIRouter()
router.include_router(generate.router)