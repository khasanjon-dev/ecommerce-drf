from django.db.models import CharField, TextField, IntegerField, JSONField, ForeignKey, CASCADE

from shared.django.model import BaseModel, DeleteModel


class Product(BaseModel, DeleteModel):
    name = CharField(max_length=255)
    brand = CharField(max_length=255)
    description = TextField()
    price = IntegerField()
    specifications = JSONField()

    """ relationships """
    author = ForeignKey('users.User', CASCADE, 'products')
    category = ForeignKey('products.Category', CASCADE)

    def __str__(self):
        return self.name
