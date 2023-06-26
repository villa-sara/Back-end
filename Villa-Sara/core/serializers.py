from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers
# from django.conf import settings
from .models import User as My_user


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = My_user
        fields = ('id', 'username', 'email', 'first_name',
                  'last_name', 'national_code', 'role', 'created_at', 'updated_at', 'image')
        # fields = '__all__'
        # extra_kwargs = {'password': {'write_only': True}}


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = My_user
        fields = ('id', 'username', 'role')


"""
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = My_user(**validated_data)
        user.set_password(password)
        user.save()
        return user
"""

"""
    class Meta:
        model = My_user
        fields = '--all--'
        # fields = ('phone_number', 'username', 'password', 'first_name', 'last_name', 'email')
"""


"""
class UserCreateSerializer(BaseUserCreateSerializer):
    phone_number = serializers.CharField(max_length=15)

    class Meta(BaseUserCreateSerializer.Meta):
        fields = '__all__'
        # fields = ['id', 'username', 'password', 'first_name', 'last_name', 'phone_number', 'email']
"""
# def validate_phone_number(self, value):
#     if settings.AUTH_USER_MODEL.objects.filter(phone_number=value).exists():
#         raise serializers.ValidationError("Phone number already exists.")
#     return value
