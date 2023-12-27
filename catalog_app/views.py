from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404

from .models import Product
from .utils import q_search


def catalog(request, slug=None):
    page = int(request.GET.get('page', 1))
    on_sale = request.GET.get('on_sale', None)
    ordering = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if slug == 'all':
        goods = Product.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = get_list_or_404(Product.objects.filter(category__slug=slug))

    if on_sale:
        goods = goods.filter(discount__gt=0)

    if ordering and ordering != 'default':
        goods = goods.order_by(ordering)

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
