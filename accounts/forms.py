from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='آدرس الکترونیک')
    mobile = forms.CharField(label='شماره همراه')
    birthday = forms.DateTimeField(label='تاریخ تولد')

    class Meta:
        model = User
        fields = ["username", "email", "mobile", "birthday", "password1", "password2"]
