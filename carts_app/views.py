from django.shortcuts import render


def cart_add(request):
    return render(request, 'carts_app/cart_add.html')


def cart_change(request):
    return render(request, 'carts_app/cart_change.html')


def cart_remove(request):
    return render(request, 'carts_app/cart_remove.html')
