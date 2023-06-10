from rest_framework.viewsets import ModelViewSet
from .models import Villa, VillaMedia
from .serializers import VillaSerializer, VillaMediaSerializer


class VillaViewSet(ModelViewSet):
    queryset = Villa.objects.all()
    serializer_class = VillaSerializer
    ordering_fields = '__all__'


class VillaMediaViewSet(ModelViewSet):
    queryset = VillaMedia.objects.all()
    serializer_class = VillaMediaSerializer
    ordering_fields = '__all__'
