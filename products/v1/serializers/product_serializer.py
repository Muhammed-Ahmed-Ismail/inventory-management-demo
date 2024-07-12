from core.serializers import BaseModelSerializer
from products.models.product import Product


class ProductSerializer(BaseModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
