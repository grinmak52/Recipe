from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Recipe(Base):
    __tablename__ = "recipes_recipe"
    title: Mapped[str]
    slug: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    description: Mapped[str]
    ingredients: Mapped[str]
    steps: Mapped[str]
    cooking_time: Mapped[int]
