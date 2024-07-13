from rest_framework import viewsets

from warehouses.models.warehouse import Warehouse
from warehouses.v1.serializers.warehouse_serializer import WarehouseSerializer


class WarehouseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows warehouses to be viewed or edited.
    """
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer