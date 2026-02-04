from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField("Название", max_length=255)
    description =  models.TextField('Описание')
    steps = models.TextField('Шаги приготовления')
    cooking_time = models.PositiveIntegerField('Время приготовления (мин)')
    image = models.ImageField('Изображение', upload_to='recipes/', blank=True, null=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='recipes')
    category = models.ManyToManyField(Category, through='RecipeCategory', related_name='recipes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Категорию рецепта'
        verbose_name_plural = 'Категории рецепта'
        unique_together = ('recipe', 'category')

    def __str__(self):
        return f'{self.recipe} -> {self.category}'