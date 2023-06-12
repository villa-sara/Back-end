from rest_framework import serializers
from .models import RentalPeriod


class RentalPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalPeriod
        fields = '__all__'
        read_only_fields = ('id')