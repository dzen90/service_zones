from zones import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'suppliers', views.SupplierViewSet, basename='supplier')
router.register(r'services', views.ServiceViewSet, basename='service')
router.register(r'zones', views.ZoneViewSet, basename='zone')

urlpatterns = [
    path('', include(router.urls))
]