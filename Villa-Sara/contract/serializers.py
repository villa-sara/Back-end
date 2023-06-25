from rest_framework import serializers
from .models import Contract


class ContractSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')
