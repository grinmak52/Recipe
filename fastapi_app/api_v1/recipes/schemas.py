from pydantic import BaseModel, ConfigDict, Field


class RecipeBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str
    ingredients: str
    steps: str
    cooking_time: int = Field(gt=0)

    category_id: int
    image: str = Field(default="", max_length=100)


class RecipeCreate(RecipeBase):
    pass


class RecipeUpdate(RecipeCreate):
    title: str | None = None
    description: str | None = None
    ingredients: str | None = None
    steps: str | None = None
    cooking_time: int | None = None
    category_id: int | None = None
    image: str | None = Field(default=None, max_length=100)


class Recipe(RecipeBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    slug: str
    author_id: int
