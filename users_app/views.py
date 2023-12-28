from django.shortcuts import render


def profile(request):
    context = {
        'title': 'FurnitureShop - Profile',
    }
    return render(request, 'users_app/profile.html', context)


def login(request):
    context = {
        'title': 'FurnitureShop - Login',
    }
    return render(request, 'users_app/login.html', context)


def register(request):
    context = {
        'title': 'FurnitureShop - Register',
    }
    return render(request, 'users_app/register.html', context)


def logout(request):
    return render(request, 'users_app/logout.html')
