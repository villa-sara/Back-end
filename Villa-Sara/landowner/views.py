from rest_framework.viewsets import ModelViewSet

from .models import VillaOwner
from .serializers import VillaOwnerSerializer


class VillaOwnerViewSet(ModelViewSet):
    queryset = VillaOwner.objects.all()
    serializer_class = VillaOwnerSerializer
    ordering_fields = '__all__'