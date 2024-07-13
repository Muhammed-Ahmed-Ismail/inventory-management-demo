from django.urls import path, include

urlpatterns = [
    path('products/', include('products.urls.v1')),
    path('warehouses/', include('warehouses.urls.v1')),
]
