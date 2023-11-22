from fastapi import APIRouter

from app.api.v1.endpoints import validate, recents
from app.api.v1.endpoints.generate import name, weapon

router = APIRouter()

# validate
router.include_router(validate.router)

# recent queries
router.include_router(recents.router)

# generators
router.include_router(name.router)
router.include_router(weapon.router)