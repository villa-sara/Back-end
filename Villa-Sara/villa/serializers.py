from rest_framework import serializers

from .models import Villa


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Villa
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')