from django.contrib.auth.mixins import UserPassesTestMixin

class RecipeOwnerRequiredMixin(UserPassesTestMixin):
    def get_object(self, queryset=None):
        if getattr(self, "object", None) is None:
            self.object = super().get_object(queryset)
        return self.object

    def test_func(self):
        return self.get_object().user == self.request.user