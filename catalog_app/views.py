from django.shortcuts import render
from .models import Product, Category


def catalog(request):
    goods = Product.objects.all()
    context = {
        'title': 'FurnitureShop - Catalog',
        'goods': goods,
    }
    return render(request, 'catalog_app/catalog.html', context)


def product(request, slug):
    item = Product.objects.get(slug=slug)
    context = {
        'title': 'FurnitureShop - Product',
        'product': item,
    }
    return render(request, 'catalog_app/product.html', context)
