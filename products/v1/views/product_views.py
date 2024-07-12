from rest_framework import viewsets

from products.models.product import Product
from products.v1.serializers.product_serializer import ProductSerializer

from django_filters import rest_framework as filters

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['name', 'description', 'code']
