from rest_framework.viewsets import ModelViewSet
from .models import Contract
from .serializers import ContractSerializer


class ContractViewSet(ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    ordering_fields = '__all__'
