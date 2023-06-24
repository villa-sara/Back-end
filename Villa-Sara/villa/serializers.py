from rest_framework import serializers
from .models import Villa, VillaMedia


class VillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Villa
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')


class VillaMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = VillaMedia
        fields = '__all__'
        read_only_fields = ('id', 'created_at')
        

# class RentalPeriodSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RentalPeriod
#         fields = '__all__'
#         read_only_fields = ('id')
#