from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Villa, VillaMedia, RentalPeriod
from .serializers import VillaSerializer, VillaMediaSerializer, RentalPeriodSerializer
from rest_framework.parsers import MultiPartParser


class VillaViewSet(ModelViewSet):
    queryset = Villa.objects.all()
    serializer_class = VillaSerializer
    ordering_fields = '__all__'
    # permission_classes = [IsAuthenticated]


"""
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated]
"""


class VillaMediaViewSet(ModelViewSet):
    queryset = VillaMedia.objects.all()
    serializer_class = VillaMediaSerializer
    ordering_fields = '__all__'
    parser_classes = [MultiPartParser]
    # permission_classes = [IsAuthenticated]


"""
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated]
"""


class RentalPeriodViewSet(ModelViewSet):
    queryset = RentalPeriod.objects.all()
    serializer_class = RentalPeriodSerializer
    ordering_fields = '__all__'
    # permission_classes = [IsAuthenticated]


"""
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated]
    """