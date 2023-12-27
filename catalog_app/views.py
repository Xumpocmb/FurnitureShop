from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Product, Category


def catalog(request, slug):
    page = int(request.GET.get('page', 1))
    goods = Product.objects.all() if slug == 'all' else get_list_or_404(Product.objects.filter(category__slug=slug))
    paginator = Paginator(goods, 3)
    current_page = paginator.page(page)
    context = {
        'title': 'FurnitureShop - Catalog',
        'goods': current_page,
        'slug_url': slug,
    }
    return render(request, 'catalog_app/catalog.html', context)


def product(request, slug):
    item = Product.objects.get(slug=slug)
    context = {
        'title': 'FurnitureShop - Product',
        'product': item,
    }
    return render(request, 'catalog_app/product.html', context)
