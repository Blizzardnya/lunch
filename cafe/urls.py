from django.urls import path, include

from . views import CategoriesAPIView, ProductsAPIView, ProductsByCategoryAPIView

urlpatterns = [
    path('category', CategoriesAPIView.as_view()),
    path('product', ProductsAPIView.as_view()),
    path('productbycategory', ProductsByCategoryAPIView.as_view()),
]