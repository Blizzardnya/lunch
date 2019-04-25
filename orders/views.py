from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer

# Create your views here.


class OrderAPIView(APIView):
    """Заказы"""
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        username = request.GET.get('username')
        orders = Order.objects.filter(customer__username=username)
        serializer = OrderSerializer(orders, many=True)
        return Response({'orders': serializer.data})
