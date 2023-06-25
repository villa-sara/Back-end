from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import User
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    lookup_field = 'pk'
    # ordering_fields = '__all__'
    # permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['GET'])
    def guest_list(self, request):
        guest = self.get_queryset().filter(role='guest')
        serializer = self.get_serializer(guest, many=True)
        # teacher_names = teachers.values_list('name', flat=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def guest(self, request, pk):
        guest = self.get_queryset().filter(role='guest', id=pk)
        serializer = self.get_serializer(guest, many=True)
        # teacher_names = teachers.values_list('name', flat=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def host_list(self, request):
        host = self.get_queryset().filter(role='host')
        serializer = self.get_serializer(host, many=True)
        # teacher_names = teachers.values_list('name', flat=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def host(self, request, pk):
        host = self.get_queryset().filter(role='host', id=pk)
        serializer = self.get_serializer(host, many=True)
        # teacher_names = teachers.values_list('name', flat=True)
        return Response(serializer.data)

    @action(detail=False, methods=['POST'])
    def create_user(self, request):
        username = request.data.get('username')
        role = request.data.get('role')
        if not username or not role:
            return Response({'detail': 'Both phone number and role are required.'}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            user = User.objects.get(username=username)
            if user:
                return Response({'detail': 'this user already exist.'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            User.objects.create_user(username=username, role=role).save()
            user = User.objects.get(username=username)
            s_user = self.get_serializer(user, many=False).data
            return Response(s_user, status=status.HTTP_200_OK)
            # return Response({'detail': 'Can\'t create User.'}, status=status.HTTP_404_NOT_FOUND)


"""
        # is_role_correct = user.check_role(role)
        if self.queryset.create(user):
        else:
            return Response({'detail': 'this user with this role is incorrect.'}, status=status.HTTP_400_BAD_REQUEST)
"""


class UserLoginView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    @action(detail=False, methods=['POST'])
    def check_user(self, request):
        username = request.data.get('username')
        role = request.data.get('role')
        if not username or not role:
            return Response({'detail': 'Both phone number and role are required.'}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        is_role_correct = user.check_role(role)
        s_user = self.get_serializer(user, many=False).data
        if is_role_correct:
            return Response(s_user, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'this user with this role is incorrect.'}, status=status.HTTP_400_BAD_REQUEST)


"""
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated]
"""