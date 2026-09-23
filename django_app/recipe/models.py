from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    step = models.TextField()
    ingredients = models.TextField()
    cooking_time = models.PositiveIntegerField(help_text="В минутах")
    image = models.ImageField(upload_to="recipe/", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='recipes')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("recipe:recipe_detail", kwargs={"slug": self.slug})