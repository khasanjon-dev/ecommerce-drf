from rest_framework.viewsets import ModelViewSet

from products.models import Product
from products.serializers.product import ProductModelSerializer
from shared.rest_framework.pagination import CustomPageNumberPagination


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    pagination_class = CustomPageNumberPagination
