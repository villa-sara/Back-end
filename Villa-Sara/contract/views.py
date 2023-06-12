from rest_framework.viewsets import ModelViewSet
from .models import Contract
from .serializers import ContractSerializer


class LandOwnerViewSet(ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    ordering_fields = '__all__'
