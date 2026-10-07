from typing import Annotated
from fastapi import APIRouter, Depends

from database.core.config import settings
from schemas.recipe import RecipeRead
from service.recipe import RecipeService
from api.dependencies import get_recipe_service

router = APIRouter(prefix=settings.api.v1.recipes, tags=['recipes'])


@router.get('/', response_model=list[RecipeRead])
async def get_recipes(service: Annotated[RecipeService, Depends(get_recipe_service)]):
    return await service.get_recipes()
