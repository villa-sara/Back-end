from rest_framework.viewsets import ModelViewSet
from .models import LandOwner
from .serializers import LandOwnerSerializer


class LandOwnerViewSet(ModelViewSet):
    queryset = LandOwner.objects.all()
    serializer_class = LandOwnerSerializer
    ordering_fields = '__all__'
