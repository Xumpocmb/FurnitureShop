from django.shortcuts import render


def index(request):
    context = {
        'title': 'FurnitureShop - Home',
    }
    return render(request, 'shop_app/index.html', context)


def about(request):
    return render(request, 'shop_app/about.html')
