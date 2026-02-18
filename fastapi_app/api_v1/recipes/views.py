from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio.session import AsyncSession

from fastapi_app.core.models import db_helper
from . import crud
from .dependencies import get_recipe_by_id
from .schemas import Recipe, RecipeCreate, RecipeUpdate

router = APIRouter(tags=["Recipes"])


@router.get("/", response_model=list[Recipe])
async def get_recipes(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_recipes(session)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
async def create_recipe(
    recipe_in: RecipeCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_recipe(session, recipe_in)


@router.get("/{recipe_id}/")
async def get_recipe(
    recipe: Recipe = Depends(get_recipe_by_id),
):
    return recipe


@router.patch("/{recipe_id}/")
async def update_recipe(
    recipe_update: RecipeUpdate,
    recipe: Recipe = Depends(get_recipe_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_recipe(session, recipe, recipe_update)


@router.delete(
    "/{recipe_id}/",
    status_code=204,
)
async def delete_recipe(
    recipe: Recipe = Depends(get_recipe_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    return await crud.delete_recipe(session, recipe)
