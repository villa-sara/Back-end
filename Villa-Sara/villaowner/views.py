from rest_framework.filters import SearchFilter
# from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import VillaOwner
from .serializers import VillaOwnerSerializer


class BusinessOwnerViewSet(ModelViewSet):
    queryset = VillaOwner.objects.all()
    serializer_class = VillaOwnerSerializer
    filter_backends = [SearchFilter]
    search_fields = ['phone_number']
    # permission_classes = [IsAuthenticated]
    ordering_fields = '__all__'