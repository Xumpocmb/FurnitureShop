from django.urls import path

from .views import catalog, product

app_name = 'catalog_app'

urlpatterns = [
    path('', catalog, name='catalog'),
    path('product/', product, name='product'),
]
