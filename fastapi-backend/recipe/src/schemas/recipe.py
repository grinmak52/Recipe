from pydantic import BaseModel, ConfigDict
from datetime import datetime

class RecipeBase(BaseModel):
    title: str
    description: str
    steps: str
    cooking_time: int

class RecipeRead(RecipeBase):
    id: int
    slug: str
    author_id: int
    created: datetime
    updated: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )

class RecipeCreate(RecipeBase):
    slug: str