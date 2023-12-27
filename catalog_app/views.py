from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def catalog(request, slug):
    if slug == 'all':
        goods = Product.objects.all()
    else:
        goods = get_object_or_404(Product.objects.filter(category__slug=slug))
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
