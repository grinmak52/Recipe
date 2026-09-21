from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("login")

class UserLoginView(LoginView):
    template_name = "accounts/login.html"

class UserLogoutView(LogoutView):
    next_page = "accounts:login"