from rest_framework import serializers
from .models import Tenant


class TenantSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()

    class Meta:
        model = Tenant
        fields = '__all__'
        read_only_fields = ('id', 'created_at')
