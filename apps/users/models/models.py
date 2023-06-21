from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db.models import ImageField, CharField, EmailField, BooleanField, TextChoices


class User(AbstractBaseUser, PermissionsMixin):
    class Role(TextChoices):
        MODERATOR = 'moderator', 'moderator'
        SIMPLE = 'simple', 'simple'

    image = ImageField(upload_to='images/users', null=True, blank=True)
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    email = EmailField(max_length=255, unique=True)
    phone = CharField(max_length=12, unique=True)
    is_active = BooleanField('active', default=False)
