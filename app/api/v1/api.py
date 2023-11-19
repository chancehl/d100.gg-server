from fastapi import APIRouter

from .endpoints import generate, validate

router = APIRouter()
router.include_router(generate.router)
router.include_router(validate.router)
