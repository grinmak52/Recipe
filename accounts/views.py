from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.forms import BaseModelForm
from django.views.generic import CreateView, View
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import redirect


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')


class MyLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')


class MyLoginView(LoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True