from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Villa, VillaMedia, State
from .serializers import VillaSerializer, VillaMediaSerializer, StateSerializer


class VillaViewSet(ModelViewSet):
    queryset = Villa.objects.all()
    serializer_class = VillaSerializer
    ordering_fields = '__all__'
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['state']
    search_fields = ['city', 'region']


class VillaMediaViewSet(ModelViewSet):
    queryset = VillaMedia.objects.all()
    serializer_class = VillaMediaSerializer
    ordering_fields = '__all__'


class StateViewSet(ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    ordering_fields = '__all__'
