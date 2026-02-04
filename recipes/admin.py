from django.contrib import admin
from .models import Recipe, Category, RecipeCategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'cooking_time', 'created_at')
    list_filter = ('categories',)
    search_fields = ('title', 'description')



admin.site.register(RecipeCategory)
