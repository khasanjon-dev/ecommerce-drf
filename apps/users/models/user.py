from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import BooleanField, TextChoices, CharField, ImageField


class UserManager(BaseUserManager):

    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('Users must have a phone number!')

        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        user = self.create_user(phone_number, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    class Role(TextChoices):
        CUSTOMER = 'customer', 'customer'
        MERCHANT = 'merchant', 'merchant'

    first_name = CharField(max_length=255)
    username = CharField(max_length=150, blank=True, null=True)
    photo = ImageField(upload_to='images/users', null=True, blank=True)
    phone_number = CharField(max_length=12, unique=True)
    role = CharField(max_length=12, choices=Role.choices, default=Role.CUSTOMER)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
