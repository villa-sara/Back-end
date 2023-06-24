from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers
# from django.conf import settings


class UserCreateSerializer(BaseUserCreateSerializer):
    phone_number = serializers.CharField(max_length=15, null=False, blank=False, unique=True, verbose_name="تلفن همراه")

    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'phone_number']

    # def validate_phone_number(self, value):
    #     if settings.AUTH_USER_MODEL.objects.filter(phone_number=value).exists():
    #         raise serializers.ValidationError("Phone number already exists.")
    #     return value
