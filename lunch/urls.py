from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/cafe/', include('cafe.urls')),
    path('api/v1/orders/', include('orders.urls')),

    path('auth/', include([
        path('', include('djoser.urls')),
        path('', include('djoser.urls.authtoken')),
        path('', include('djoser.urls.jwt')),
    ])),
]
