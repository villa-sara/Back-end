from rest_framework import serializers
from .models import LandOwner


class LandOwnerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()

    class Meta:
        model = LandOwner
        fields = '__all__'
        # read_only_fields = ('id', 'created_at')
