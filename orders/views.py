from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.parsers import JSONParser
from rest_framework.generics import get_object_or_404

from .models import Order, OrderItem
from cafe.models import Product
from .serializers import OrderSerializer, OrderItemSerializer

# Create your views here.


class OrderAPIView(APIView):
    """Заказы"""
    permission_classes = [permissions.IsAuthenticated, ]
    parser_classes = (JSONParser, )

    def get(self, request):
        username = request.GET.get('username')
        orders = Order.objects.filter(customer__username=username)
        serializer = OrderSerializer(orders, many=True)
        return Response({'orders': serializer.data})

    def post(self, request):
        username = request.data['user']
        products = request.data['products']

        try:
            user = get_object_or_404(User, username=username)

            order = Order.objects.create(customer=user)
            print(order)

            for product_item in products:
                product = get_object_or_404(Product, pk=product_item['id'])

                OrderItem.objects.create(
                    order=order,
                    product=product,
                    price=product.price,
                    quantity=product_item['quantity']
                )

            return Response(status=201)
        except:
            return Response(status=400)
