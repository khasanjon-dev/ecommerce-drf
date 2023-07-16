from rest_framework.generics import ListAPIView

from products.models import Category
from products.serializers.category import CategoryModelSerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
