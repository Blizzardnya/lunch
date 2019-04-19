from django.contrib import admin

from .models import Category, Product
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'available', 'created_at', 'updated_at')
    list_editable = ('available', )
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'available', 'created_at', 'updated_at')
    list_editable = ('price', 'available')
    prepopulated_fields = {'slug': ('name', )}
