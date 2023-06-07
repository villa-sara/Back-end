from rest_framework import serializers

from .models import Tenant


class TenantOwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tenant
        fields = '__all__'
        read_only_fields = ('id', 'created_at')