from django.contrib import auth
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users_app.forms import UserLoginForm


def profile(request):
    context = {
        'title': 'FurnitureShop - Profile',
    }
    return render(request, 'users_app/profile.html', context)


def login(request):
    context = {
        'title': 'FurnitureShop - Login',
    }
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('users_app:profile'))
    else:
        form = UserLoginForm()
    context['form'] = form
    return render(request, 'users_app/login.html', context)


def register(request):
    context = {
        'title': 'FurnitureShop - Register',
    }
    return render(request, 'users_app/register.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('shop_app:index'))
