from django.urls import path
from django.urls.conf import include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('inventory_management_demo.api.v1'))
]