from unicodedata import name
from django.urls import path
from .views import register, sign_in


urlpatterns = [
    path('register-user', register, name="register_user"),
    path('login', sign_in, name='login'),
]