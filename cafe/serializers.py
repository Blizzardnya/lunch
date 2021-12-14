from rest_framework import serializers

from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    """Сериализация категорий"""

    class Meta:
        model = Category
        fields = ('id', 'name')


class ProductSerializer(serializers.ModelSerializer):
    """Сериализация продуктов"""
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'category')


class ProductLessSerializer(serializers.ModelSerializer):
    """Сериализация продуктов без цены и описания (для заказов)"""
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ('id', 'name',  'category')
