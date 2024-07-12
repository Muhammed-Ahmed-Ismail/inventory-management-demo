from django_filters import rest_framework as filters

from products.models.product import Product


class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    description = filters.CharFilter(lookup_expr='icontains')
    code = filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Product
        fields = ['name', 'description', 'code']