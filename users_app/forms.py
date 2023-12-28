from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'password']

    # username = forms.CharField(widget=forms.TextInput(attrs={
    #     'class': 'form-control',
    #     'id': "username",
    #     'autofocus': True,
    #     'placeholder': "Введите ваше имя пользователя",
    # }))
    #
    # password = forms.CharField(widget=forms.PasswordInput(attrs={
    #     'class': 'form-control',
    #     'id': "password",
    #     'placeholder': "Введите ваш пароль",
    # }))
