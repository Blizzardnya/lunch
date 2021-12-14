from django.db.models import Q
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoriesAPIView(APIView):
    """Категории"""
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        categories = Category.objects.filter(available=True)
        serializer = CategorySerializer(categories, many=True)
        return Response({'categories': serializer.data})


class ProductsByCategoryAPIView(APIView):
    """Продукты"""
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        category = request.GET.get('category')
        products = Product.objects.filter(Q(category=category) & Q(available=True))
        serializer = ProductSerializer(products, many=True)
        return Response({'products': serializer.data})


class ProductsAPIView(APIView):
    """Продукты"""
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        products = Product.objects.filter(available=True)
        serializer = ProductSerializer(products, many=True)
        return Response({'products': serializer.data})
