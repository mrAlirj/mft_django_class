from django.urls import path
from .views import register


urlpatterns = [
    path('register-user', register, name="register_user")
]