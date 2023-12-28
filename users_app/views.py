from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users_app.forms import UserLoginForm, UserRegistrationForm


@login_required(login_url='users_app:login')
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
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            # user = form.instance
            return HttpResponseRedirect(reverse('users_app:login'))
    else:
        form = UserRegistrationForm()
    context['form'] = form
    return render(request, 'users_app/register.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('shop_app:index'))
