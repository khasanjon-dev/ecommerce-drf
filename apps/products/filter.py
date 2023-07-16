from django_filters import FilterSet, NumberFilter

from products.models import Product


class ProductFilterSet(FilterSet):
    from_price = NumberFilter('price', 'gte')
    to_price = NumberFilter('price', 'lte')

    class Meta:
        model = Product
        fields = {
            'name': ['iexact'],
            'price': ['exact'],
        }
