from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_app.core.models import db_helper, Recipe as RecipeModel
from fastapi_app.core.security import decode_access_token

from . import crud

http_bearer = HTTPBearer(auto_error=False)


async def get_recipe_by_id(
    recipe_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> RecipeModel:
    recipe = await crud.get_recipe(session, recipe_id)
    if recipe:
        return recipe

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Recipe not found",
    )


async def get_current_user_id(
    credentials: HTTPAuthorizationCredentials | None = Depends(http_bearer),
) -> int:
    if credentials is None or not credentials.credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing bearer token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    try:
        return decode_access_token(credentials.credentials)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
