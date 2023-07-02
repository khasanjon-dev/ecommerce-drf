from django.db.models import CharField, TextField, IntegerField, JSONField, ForeignKey, CASCADE, Model, ImageField

from shared.django.model import BaseModel, DeleteModel


class Product(BaseModel, DeleteModel):
    name = CharField(max_length=255)
    description = TextField()
    price = IntegerField()
    specifications = JSONField(default=dict)

    """ relationships """
    author = ForeignKey('users.User', CASCADE, 'products')
    category = ForeignKey('products.Category', CASCADE)
    brand = ForeignKey('products.Brand', CASCADE)

    def __str__(self):
        return self.name


class ProductImage(Model):
    image = ImageField(upload_to='images/products')
    product = ForeignKey('Product', CASCADE, 'images')

    def __str__(self):
        return self.product.name
