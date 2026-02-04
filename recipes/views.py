from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Recipe
from .forms import RecipeForm


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/index.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        return Recipe.objects.order_by('?')[:5]


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/form.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/form.html'
    success_url = reverse_lazy('index')

    def get_queryset(self):
        return Recipe.objects.filter(author=self.request.user)

