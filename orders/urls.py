from django.urls import path, include

from . views import OrderAPIView

urlpatterns = [
    path('order', OrderAPIView.as_view()),
]