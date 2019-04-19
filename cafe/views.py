from django.shortcuts import render
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
# Create your views here.


class CategoriesAPIView(APIView):
    """Категории"""

    def get(self, request):
        categories = Category.objects.filter(available=True)
        serializer = CategorySerializer(categories, many=True)
        return Response({'data': serializer.data})


class ProductsAPIView(APIView):
    """Продукты"""

    def get(self, request):
        category = request.GET.get('category')
        products = Product.objects.filter(Q(category=category) & Q(available=True))
        serializer = ProductSerializer(products, many=True)
        return Response({'data': serializer.data})
