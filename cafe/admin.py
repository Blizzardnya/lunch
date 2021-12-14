from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'available', 'created_at', 'updated_at')
    list_editable = ('available', )
    list_filter = ('available', 'created_at', 'updated_at')
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'available', 'created_at', 'updated_at')
    list_editable = ('price', 'available')
    list_filter = ('available', 'created_at', 'updated_at')
    search_fields = ['name', 'category__name']
    prepopulated_fields = {'slug': ('name', )}
