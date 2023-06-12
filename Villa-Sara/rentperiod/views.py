from rest_framework.viewsets import ModelViewSet
from .models import RentalPeriod
from .serializers import RentalPeriodSerializer


class VillaViewSet(ModelViewSet):
    queryset = RentalPeriod.objects.all()
    serializer_class = RentalPeriodSerializer
    ordering_fields = '__all__'
