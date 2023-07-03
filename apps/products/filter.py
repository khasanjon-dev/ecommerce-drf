from django_filters import FilterSet

from products.models import Product


class ProductFilterSet(FilterSet):
    class Meta:
        model = Product
        fields = {
            'name': ['exact'],
        }
