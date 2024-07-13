from rest_framework import serializers

from core.serializers import BaseModelSerializer
from products.models import Product
from warehouses.exceptions.not_sufficient_quantity_exception import NotSufficientQuantityException
from warehouses.models import Warehouse
from warehouses.models.inventory_entry import InventoryEntry


class InventoryEntrySerializer(serializers.Serializer):
    quantity = serializers.IntegerField()
    warehouse = serializers.PrimaryKeyRelatedField(queryset=Warehouse.objects.all())
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    def validate_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError('Quantity must be greater than 0')

        return value

    def to_internal_value(self, data):
        data['warehouse'] = self.context['request'].parser_context['kwargs']['warehouse_id']
        return super().to_internal_value(data)

    def create(self, validated_data):
        quantity = validated_data.pop('quantity')
        warehouse = validated_data.pop('warehouse')
        product = validated_data.pop('product')
        if self.context.get('add', False):
            return InventoryEntry.add_product_to_warehouse(product, quantity, warehouse)
        if self.context.get('draw', True):
            try:
                return InventoryEntry.draw_product_from_warehouse(product, quantity, warehouse)
            except NotSufficientQuantityException:
                raise serializers.ValidationError('Not sufficient quantity to draw')
        raise serializers.ValidationError('Invalid request')
