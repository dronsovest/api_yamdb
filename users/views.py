from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import CustomUser
from users.serializers import (EmailSerializer,
                               UserSerializer,
                               GetTokenSerializer, )

from .permissions import IsAdmin


class GetConfirmationCode(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get("email")
        user, created = CustomUser.objects.get_or_create(email=email)
        confirmation_code = make_password(email)
        if created:
            user.username = email
            user.confirmation_code = confirmation_code
            user.save()
        subject = "Регистрация в YaMDB"
        body = (
            f"Для продолжения регистрации {user.email} в YaMDB и\n"
            f"получения токена отправьте запрос на\n"
            f"http://127.0.0.1:8000/api/v1/auth/email/ с\n"
            f"параметрами email и confirmation_code.\n\n"
            f"Ваш confirmation_code: {user.confirmation_code}\n"
        )
        send_mail(
            subject, body, "yamdb@yandex.test", [user.email, ],
            fail_silently=False,
        )

        return Response(serializer.data, status=200)


class GetToken(APIView):
    def post(self, request):
        serializer = GetTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get("email")
        code = serializer.data.get("confirmation_code")
        user = get_object_or_404(CustomUser, email=email,
                                 confirmation_code=code)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({'token': f'{refresh.access_token}'}, status=200)
        return Response(status=400)


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsAdmin,)
    lookup_field = "username"
