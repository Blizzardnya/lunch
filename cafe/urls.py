from django.urls import path, include

from . views import CategoriesAPIView, ProductsAPIView

urlpatterns = [
    path('category', CategoriesAPIView.as_view()),
    path('product', ProductsAPIView.as_view()),
]