from fastapi import APIRouter

from .endpoints import generate, validate, recents

router = APIRouter()
router.include_router(generate.router)
router.include_router(validate.router)
router.include_router(recents.router)
