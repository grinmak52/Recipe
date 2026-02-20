from fastapi import APIRouter

from .auth import router as auth_router
from .recipes.views import router as recipes_router

router = APIRouter()
router.include_router(auth_router)
router.include_router(recipes_router, prefix="/recipes")
