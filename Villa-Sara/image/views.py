from rest_framework.viewsets import ModelViewSet

from .models import Image
from .serializers import ImageSerializer


class CollectionViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
