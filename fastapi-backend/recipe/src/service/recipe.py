from sqlalchemy.ext.asyncio import AsyncSession

from repository.recipe import RecipeRepository


class RecipeService:
    def __init__(self, recipe_repository: RecipeRepository):
        self.recipe_repository = recipe_repository

    async def get_recipes(self):
        return await self.recipe_repository.get_all()