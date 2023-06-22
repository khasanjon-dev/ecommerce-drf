from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import update_last_login
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings

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


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        phone_number = attrs['phone_number']
        password = attrs['password']
        if not User.objects.filter(phone_number=phone_number).exists():
            raise ValidationError('User is not registered!')
        user = User.objects.filter(phone_number=phone_number).first()
        if not user.check_password(password):
            raise ValidationError('Password is not correct!')

        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data
