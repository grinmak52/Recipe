from django.urls import path
from . import views

app_name = 'recipe'

urlpatterns = [
    path("", views.RecipeView.as_view(), name="recipe"),
    path("<slug:slug>", views.RecipeDetailView.as_view(), name="recipe_detail"),
    path("create/", views.RecipeCreateView.as_view(), name="recipe_create"),
]
