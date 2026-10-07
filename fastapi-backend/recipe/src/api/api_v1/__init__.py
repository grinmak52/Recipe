from fastapi import APIRouter

from database.core.config import settings

from .recipes import router as recipes_router

router = APIRouter(prefix=settings.api.v1.prefix)
router.include_router(recipes_router)