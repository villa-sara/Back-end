from rest_framework import serializers

from .models import VillaOwner

class VillaOwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = VillaOwner
        fields = '__all__'
        read_only_fields = ('id', 'created_at')