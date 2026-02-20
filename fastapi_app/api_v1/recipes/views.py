from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio.session import AsyncSession

from fastapi_app.core.models import db_helper
from . import crud
from .dependencies import get_current_user_id, get_recipe_by_id
from .schemas import (
    MessageResponse,
    Recipe as RecipeSchema,
    RecipeCreate,
    RecipeUpdate,
)

router = APIRouter(tags=["Recipes"])


@router.get("/", response_model=list[RecipeSchema])
async def get_recipes(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_recipes(session)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=MessageResponse,
)
async def create_recipe(
    recipe_in: RecipeCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
    author_id: int = Depends(get_current_user_id),
):
    try:
        recipe = await crud.create_recipe(session, recipe_in, author_id=author_id)
        return MessageResponse(message="Recipe created successfully", recipe_id=recipe.id)
    except IntegrityError as exc:
        msg = str(getattr(exc, "orig", exc)).lower()
        if "duplicate key value" in msg or "unique" in msg:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Recipe with same title/slug already exists",
            )
        if "foreign key" in msg:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid author_id or category_id",
            )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Integrity error",
        )


@router.get("/{recipe_id}/", response_model=RecipeSchema)
async def get_recipe(
    recipe=Depends(get_recipe_by_id),
):
    return recipe


@router.patch("/{recipe_id}/", response_model=MessageResponse)
async def update_recipe(
    recipe_update: RecipeUpdate,
    recipe=Depends(get_recipe_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    try:
        updated = await crud.update_recipe(session, recipe, recipe_update)
        return MessageResponse(message="Recipe updated successfully", recipe_id=updated.id)
    except IntegrityError as exc:
        msg = str(getattr(exc, "orig", exc)).lower()
        if "duplicate key value" in msg or "unique" in msg:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Recipe with same title/slug already exists",
            )
        if "foreign key" in msg:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid author_id or category_id",
            )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Integrity error",
        )


@router.delete(
    "/{recipe_id}/",
    status_code=status.HTTP_200_OK,
    response_model=MessageResponse,
)
async def delete_recipe(
    recipe=Depends(get_recipe_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> MessageResponse:
    await crud.delete_recipe(session, recipe)
    return MessageResponse(message="Recipe deleted successfully", recipe_id=recipe.id)
