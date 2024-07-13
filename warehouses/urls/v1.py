from django.urls import path
from rest_framework import routers

from warehouses.v1.views.warehouse_view import WarehouseViewSet
from warehouses.v1.views.inventory_entries_view import InventoryEntriesViewSet

router = routers.DefaultRouter()
router.register(r'', WarehouseViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('<int:warehouse_id>/products', InventoryEntriesViewSet.as_view({'get': 'list'})),
    path('<int:warehouse_id>/products/add', InventoryEntriesViewSet.as_view({'post': 'add'})),
    path('<int:warehouse_id>/products/draw', InventoryEntriesViewSet.as_view({'post': 'draw'})),
    path('<int:warehouse_id>/products/<int:product_id>', InventoryEntriesViewSet.as_view({'get': 'retrieve'})),
]
