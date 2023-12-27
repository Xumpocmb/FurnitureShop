from django.shortcuts import render


def catalog(request):
    # 04:39
    context = {
        'title': 'FurnitureShop - Catalog',
    }
    return render(request, 'catalog_app/catalog.html', context)


def product(request):
    context = {
        'title': 'FurnitureShop - Product',
    }
    return render(request, 'catalog_app/product.html', context)
