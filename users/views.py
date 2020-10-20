from rest_framework import viewsets
from rest_framework.views import APIView

from users.models import CustomUser
from .permissions import IsAdmin
from users.serializers import UserSerializer


class GetConfirmationCode(APIView):
    pass


class GetToken(APIView):
    pass


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdmin,)
    lookup_field = 'username'
