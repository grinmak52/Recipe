from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database.orm import db_helper
from repository.recipe import RecipeRepository
from service.recipe import RecipeService


async def get_recipe_repository(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
) -> RecipeRepository:
    return RecipeRepository(session)


def get_recipe_service(
    recipe_repository: Annotated[
        RecipeRepository,
        Depends(get_recipe_repository),
    ],
) -> RecipeService:
    return RecipeService(recipe_repository)