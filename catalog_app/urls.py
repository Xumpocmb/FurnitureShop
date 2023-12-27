from django.urls import path

from .views import catalog, product

app_name = 'catalog_app'

urlpatterns = [
    path('search/', catalog, name='search'),
    path('<slug:slug>/', catalog, name='catalog'),
    path('product/<slug:slug>/', product, name='product'),
]
