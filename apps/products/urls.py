from django.urls import path, include
from rest_framework.routers import DefaultRouter

from products.views.product import ProductModelViewSet

router = DefaultRouter()
router.register('', ProductModelViewSet, 'products')

urlpatterns = [
    path('', include(router.urls)),
]
