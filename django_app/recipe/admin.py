from django.contrib import admin

from recipe.models import Recipe, Category


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "description", "category", "created", "updated"
    list_display_links = "pk", "name"
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "pk", "name",
    list_display_links = "pk", "name"
    prepopulated_fields = {"slug": ("name",)}