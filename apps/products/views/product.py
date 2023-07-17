from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_elasticsearch_dsl_drf.constants import SUGGESTER_COMPLETION
from django_elasticsearch_dsl_drf.filter_backends import SearchFilterBackend, SuggesterFilterBackend
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from products.documents import ProductDocument
from products.filter import ProductFilterSet
from products.models import Product
from products.serializers.product import ProductModelSerializer, ProductDocumentSerializer
from shared.rest_framework.pagination import CustomPageNumberPagination


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilterSet


class ProductDocumentViewSet(DocumentViewSet):
    document = ProductDocument
    serializer_class = ProductDocumentSerializer

    filter_backends = [SearchFilterBackend, SuggesterFilterBackend]
    search_fields = (
        'name',
        'description',
    )

    suggester_fields = {
        'name': {
            'field': 'name.suggest',
            'suggester': [
                SUGGESTER_COMPLETION
            ]
        }
    }

    @method_decorator(cache_page(60 * 60 * 2))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
