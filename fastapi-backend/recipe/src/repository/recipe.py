from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.orm.models import Recipe


class RecipeRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self):
        result = await self.session.execute(select(Recipe))
        return result.scalars().all()