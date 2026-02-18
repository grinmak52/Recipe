from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_app.core.models import db_helper, Recipe

from . import crud


async def get_recipe_by_id(
    recipe_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Recipe:
    recipe = await crud.get_recipe(session, recipe_id)
    if recipe:
        return recipe

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Recipe not found",
    )
