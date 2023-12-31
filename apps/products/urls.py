from django.urls import path, include
from rest_framework.routers import DefaultRouter

from products.views.category import CategoryListAPIView
from products.views.product import ProductModelViewSet, ProductDocumentViewSet

router = DefaultRouter()
router.register('', ProductModelViewSet, 'products')
router.register('search', ProductDocumentViewSet, 'search')
urlpatterns = [
    path('', include(router.urls)),
    path('category', CategoryListAPIView.as_view(), name='category'),
]
