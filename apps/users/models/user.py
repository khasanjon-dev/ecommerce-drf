from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import BooleanField, TextChoices


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
        MERCHANT = 'merchant', 'merchant'
        CUSTOMER = 'customer', 'customer'

    first_name = models.CharField(max_length=255)
    username = models.CharField(max_length=150, blank=True, null=True)
    photo = models.ImageField(upload_to='images/users', null=True, blank=True)
    phone_number = models.CharField(max_length=12, unique=True)
    role = models.CharField(max_length=12, choices=Role.choices, default=Role.CUSTOMER)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
