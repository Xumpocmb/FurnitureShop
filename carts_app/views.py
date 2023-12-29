from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from carts_app.models import Cart
from carts_app.utils import get_user_carts
from catalog_app.models import Product


def cart_add(request):
    product = Product.objects.get(id=request.POST.get('product_id'))
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user, product=product)
        if cart.exists():
            cart.update(quantity=F('quantity') + 1)
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)
    user_carts = get_user_carts(request)
    cart_items_html = render_to_string('cart_modal.html',
                                       {'carts': user_carts},
                                       request=request)
    response_data = {
        "message": "Товар добавлен в корзину",
        "cart_items_html": cart_items_html,
    }

    return JsonResponse(response_data)


def cart_change(request, product_slug):
    return render(request, 'carts_app/cart_change.html')


def cart_remove(request, cart_id):
    Cart.objects.get(id=cart_id).delete()
    return redirect(request.META.get('HTTP_REFERER'))
