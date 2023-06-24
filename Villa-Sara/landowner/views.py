from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import LandOwner
from .serializers import LandOwnerSerializer


class LandOwnerViewSet(ModelViewSet):
    queryset = LandOwner.objects.all()
    serializer_class = LandOwnerSerializer
    ordering_fields = '__all__'
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated]
