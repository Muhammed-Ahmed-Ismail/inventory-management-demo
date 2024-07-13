from core.serializers import BaseModelSerializer
from warehouses.models.warehouse import Warehouse
from rest_framework import serializers


class WarehouseSerializer(BaseModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'

    def to_representation(self, instance: Warehouse):
        to_rep = super().to_representation(instance)
        to_rep.update({
            'location': instance.location
        })
        return to_rep

    def validate_longitude(self, value):
        if value < -180 or value > 180:
            raise serializers.ValidationError('Longitude must be between -180 and 180')
        return value

    def validate_latitude(self, value):
        if value < -90 or value > 90:
            raise serializers.ValidationError('Latitude must be between -90 and 90')
        return value
