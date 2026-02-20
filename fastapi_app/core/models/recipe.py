from sqlalchemy import BigInteger, ForeignKey, Integer, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Recipe(Base):
    __tablename__ = "recipes_recipe"

    title: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    slug: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        index=True,
        nullable=False,
    )
    description: Mapped[str] = mapped_column(Text, nullable=False)
    ingredients: Mapped[str] = mapped_column(Text, nullable=False)
    steps: Mapped[str] = mapped_column(Text, nullable=False)
    cooking_time: Mapped[int] = mapped_column(SmallInteger, nullable=False)

    # Django ImageField stores string path (blank=True, usually NOT NULL)
    image: Mapped[str] = mapped_column(String(100), nullable=False, default="")

    author_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("auth_user.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    category_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("recipes_category.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
