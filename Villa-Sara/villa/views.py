from rest_framework.filters import SearchFilter
# from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Villa
from .serializers import VillaSerializer


class VillaViewSet(ModelViewSet):
    queryset = Villa.objects.all()
    serializer_class = VillaSerializer
    # filter_backends = [SearchFilter]
    # search_fields = ['phone_number']
    # permission_classes = [IsAuthenticated]
    ordering_fields = '__all__'