from django.urls import path
from .views import (
    RecipeListView,
    RecipeDetailView,
    RecipeCreateView,
    RecipeUpdateView, CategoryRecipeListView
)

urlpatterns = [
    path("", RecipeListView.as_view(), name="index"),
    path('category/<slug:slug>/>', CategoryRecipeListView.as_view(), name="category"),
    path("recipe/<int:pk>", RecipeDetailView.as_view(), name="detail"),
    path("recipe/add", RecipeCreateView.as_view(), name="add"),
    path("recipe/<int:pk>/edit", RecipeUpdateView.as_view(), name="edit"),
]