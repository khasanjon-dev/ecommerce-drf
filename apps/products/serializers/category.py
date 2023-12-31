from rest_framework.serializers import ModelSerializer

from products.models import Category


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
