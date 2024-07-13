from django.db import transaction
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from warehouses.models import Warehouse
from warehouses.models.inventory_entry import InventoryEntry
from warehouses.v1.serializers.inventory_entry_serializer import InventoryEntrySerializer


class InventoryEntriesViewSet(viewsets.ModelViewSet):
    serializer_class = InventoryEntrySerializer

    @action(detail=True, methods=['post'])
    def add(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'add': True, 'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def draw(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'draw': True, 'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        warehouse_id = self.kwargs['warehouse_id']
        return InventoryEntry.objects.filter(warehouse_id=warehouse_id)

    def get_object(self):
        warehouse_id = self.kwargs['warehouse_id']
        product_id = self.kwargs['product_id']
        return InventoryEntry.objects.get(warehouse_id=warehouse_id, product_id=product_id)
