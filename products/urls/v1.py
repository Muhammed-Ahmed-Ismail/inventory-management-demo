from rest_framework import routers

from products.v1.views.product_views import ProductViewSet

router = routers.DefaultRouter()
router.register(r'', ProductViewSet)

urlpatterns = router.urls