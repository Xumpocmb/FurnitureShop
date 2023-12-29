from django.db.models import F
from django.shortcuts import render, redirect

from carts_app.models import Cart
from catalog_app.models import Product


def cart_add(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user, product=product)
        if cart.exists():
            cart.update(quantity=F('quantity') + 1)
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)
    return redirect(request.META.get('HTTP_REFERER'))


def cart_change(request, product_slug):
    return render(request, 'carts_app/cart_change.html')


def cart_remove(request, cart_id):
    Cart.objects.get(id=cart_id).delete()
    return redirect(request.META.get('HTTP_REFERER'))
