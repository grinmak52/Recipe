from django.urls import path
from .views import RegisterView, MyLogoutView, MyLoginView

urlpatterns = [
    path('Login/', MyLoginView.as_view(), name='login'),
    path('Logout/', MyLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]