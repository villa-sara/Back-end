from rest_framework.viewsets import ModelViewSet

from .models import Tenant
from .serializers import TenantSerializer


class VillaOwnerViewSet(ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    ordering_fields = '__all__'