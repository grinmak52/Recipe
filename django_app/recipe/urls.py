from django.urls import path
from . import views

app_name = 'recipe'

urlpatterns = [
    path("", views.RecipeView.as_view(), name="recipe_list"),
    path("create/", views.RecipeCreateView.as_view(), name="recipe_create"),
    path("<slug:slug>/", views.RecipeDetailView.as_view(), name="recipe_detail"),
    path("<slug:slug>/update/", views.RecipeUpdateView.as_view(), name="recipe_update"),
    path("<slug:slug>/delete/", views.RecipeDeleteView.as_view(), name="recipe_delete"),
]
