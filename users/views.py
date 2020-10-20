from django.core.mail import send_mail
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.models import CustomUser
from .permissions import IsAdmin
from users.serializers import UserSerializer, EmailSerializer


class GetConfirmationCode(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        email = serializer.data.get("email")
        user, created = CustomUser.objects.get_or_create(
            username=email, email=email)

        confirmation_code = ???????
        send_mail(
            f"Код подтверждения для регистрации в YaMDB",
            f"{confirmation_code}",
            'yamdb@yandex.test',
            [f"{email}"],
            fail_silently=False,
        )
        return Response(
            {"result": "Код подтверждения отправлен на почту"}, status=200
        )

    def send_msg(email, name, title, artist, genre, price, comment):
        subject = f"Обмен {artist}-{title}"
        body = f"""Предложение на обмен диска от {name} ({email})

        Название: {title}
        Исполнитель: {artist}
        Жанр: {genre}
        Стоимость: {price}
        Комментарий: {comment}

        """
        send_mail(
            subject, body, email, ["admin@rockenrolla.net", ],
        )

    pass


class GetToken(APIView):
    pass


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdmin, IsAuthenticated,)
    lookup_field = 'username'
