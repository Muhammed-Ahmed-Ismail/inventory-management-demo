from rest_framework import routers

from warehouses.v1.views.warehouse_view import WarehouseViewSet

router = routers.DefaultRouter()
router.register(r'', WarehouseViewSet)

urlpatterns = router.urls