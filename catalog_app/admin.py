from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ['name']}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'slug', 'description', 'image',
        'price', 'discount', 'quantity', 'available',
        'created_at', 'category'
    ]
    prepopulated_fields = {'slug': ['name']}
    search_fields = ['name', 'description']
    list_filter = ['available', 'category']
    readonly_fields = ['created_at']
