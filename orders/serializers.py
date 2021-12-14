from django.contrib.auth.models import User
from rest_framework import serializers

from cafe.serializers import ProductLessSerializer
from .models import Order, OrderItem


class UserSerializer(serializers.ModelSerializer):
    """Сериальзация пользователей"""

    class Meta:
        model = User
        fields = ('username', 'first_name')


class OrderSerializer(serializers.ModelSerializer):
    """Сериализация заказов"""
    # customer = UserSerializer()
    order_items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('id', 'created', 'updated', 'get_total_cost', 'status', 'order_items')

    def get_order_items(self, instance):
        order_items = instance.items.all()
        return OrderItemSerializer(order_items, many=True).data


class OrderItemSerializer(serializers.ModelSerializer):
    """Сериализация строк заказа"""
    # order = OrderSerializer()
    product = ProductLessSerializer()

    class Meta:
        model = OrderItem
        fields = ('product', 'price', 'quantity', 'get_cost')
