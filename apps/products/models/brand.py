from django.db.models import Model, CharField


class Brand(Model):
    name = CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
