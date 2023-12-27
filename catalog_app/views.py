from django.shortcuts import render
from .models import Product, Category


def catalog(request):
    goods = Product.objects.all()
    context = {
        'title': 'FurnitureShop - Catalog',
        'goods': goods,
    }
    return render(request, 'catalog_app/catalog.html', context)


def product(request):
    context = {
        'title': 'FurnitureShop - Product',
    }
    return render(request, 'catalog_app/product.html', context)
