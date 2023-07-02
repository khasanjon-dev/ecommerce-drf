from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer, Serializer

from users.models import User
from utils.validators import validate_phone


class UserModelSerializer(ModelSerializer):
    password = CharField(write_only=True, max_length=12, required=True, validators=[validate_password])
    phone_number = CharField(max_length=12, default=998)

    class Meta:
        model = User
        fields = [
            'first_name',
            'phone_number',
            'password',
            'role',
            'photo',
        ]

    def validate(self, attrs):

        # validate phone number
        validate_phone(attrs['phone_number'])

        if password := attrs.get('password'):
            attrs['password'] = make_password(password)
        if User.objects.filter(phone_number=attrs['phone_number']).exists():
            raise ValidationError('Phone number has already exist!')
        return attrs


class SendCode(Serializer):
    phone_number = CharField(max_length=12)

    def validate(self, attrs):
        phone_number = attrs['phone_number']
        validate_phone(phone_number)
