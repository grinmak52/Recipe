from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from recipe.forms import RecipeForm
from recipe.mixins import RecipeOwnerRequiredMixin
from recipe.models import Recipe
from recipe.service import generate_unique_slug


class RecipeView(ListView):
    model = Recipe
    paginate_by = 12


class RecipeDetailView(DetailView):
    queryset = Recipe.objects.select_related("user", "category")


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.slug = generate_unique_slug(form.instance.name)
        messages.success(self.request, f'Рецепт "{form.instance.name}" успешно создан!')
        return super().form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, RecipeOwnerRequiredMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm

    def test_func(self):
        result = super().test_func()
        self._old_name = self.object.name
        return result

    def form_valid(self, form):
        if form.instance.name != self._old_name:
            form.instance.slug = generate_unique_slug(form.instance.name, instance_pk=form.instance.pk)
        messages.success(self.request, f'Рецепт "{form.instance.name}" обновлён!')
        return super().form_valid(form)


class RecipeDeleteView(LoginRequiredMixin, RecipeOwnerRequiredMixin, DeleteView):
    model = Recipe
    success_url = reverse_lazy("recipe:recipe_list")

    def form_valid(self, form):
        messages.success(self.request, f'Рецепт "{self.object.name}" удалён.')
        return super().form_valid(form)