from pydantic import BaseModel, ConfigDict, model_validator


class RecipeBase(BaseModel):
    title: str
    description: str
    ingredients: str
    steps: str
    cooking_time: int


class RecipeCreate(RecipeBase):
    pass


class RecipeUpdate(RecipeCreate):
    title: str | None = None
    description: str | None = None
    ingredients: str | None = None
    steps: str | None = None
    cooking_time: int | None = None


class Recipe(RecipeBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    slug: str
