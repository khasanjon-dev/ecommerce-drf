from django.contrib import admin
from django.contrib.admin import ModelAdmin, StackedInline

from products.models import Product, Category, Brand
from products.models.product import ProductImage


class ProductImageStackedInline(StackedInline):
    model = ProductImage
    max_num = 3


@admin.register(Product)
class ProductModelAdmin(ModelAdmin):
    inlines = (ProductImageStackedInline,)


@admin.register(ProductImage)
class ProductImageModelAdmin(ModelAdmin):
    pass


@admin.register(Category)
class CategoryModelAdmin(ModelAdmin):
    pass


@admin.register(Brand)
class BrandModelAdmin(ModelAdmin):
    pass
