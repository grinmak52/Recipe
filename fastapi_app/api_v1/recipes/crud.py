from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from slugify import slugify

from .schemas import RecipeCreate, RecipeUpdate
from fastapi_app.core.models import Recipe


async def get_recipes(session: AsyncSession) -> list[Recipe]:
    stmt = select(Recipe).order_by(Recipe.id)
    result: Result = await session.execute(stmt)
    recipes = result.scalars().all()
    return list(recipes)


async def get_recipe(
    session: AsyncSession,
    recipe_id: int,
) -> Recipe | None:
    return await session.get(Recipe, recipe_id)


async def create_recipe(
    session: AsyncSession,
    recipe_in: RecipeCreate,
    author_id: int,
) -> Recipe | None:
    recipe_data = recipe_in.model_dump()
    recipe_data["slug"] = slugify(recipe_in.title)
    recipe_data.setdefault("image", "")
    recipe_data["author_id"] = author_id

    recipe = Recipe(**recipe_data)
    session.add(recipe)
    try:
        await session.commit()
    except IntegrityError:
        await session.rollback()
        raise
    await session.refresh(recipe)
    return recipe


async def update_recipe(
    session: AsyncSession,
    recipe: Recipe,
    recipe_update: RecipeUpdate,
) -> Recipe:
    for name, value in recipe_update.model_dump(exclude_unset=True).items():
        if name == "image" and value is None:
            value = ""
        setattr(recipe, name, value)
    try:
        await session.commit()
    except IntegrityError:
        await session.rollback()
        raise
    await session.refresh(recipe)
    return recipe


async def delete_recipe(
    session: AsyncSession,
    recipe: Recipe,
) -> None:
    await session.delete(recipe)
    await session.commit()
