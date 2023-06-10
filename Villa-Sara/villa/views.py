from rest_framework.viewsets import ModelViewSet
from .models import Villa
from .serializers import VillaSerializer


class VillaViewSet(ModelViewSet):
    queryset = Villa.objects.all()
    serializer_class = VillaSerializer
    ordering_fields = '__all__'
