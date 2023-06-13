from rest_framework import serializers
from .models import LandOwner


class LandOwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = LandOwner
        fields = '__all__'
        read_only_fields = ('id', 'created_at')
