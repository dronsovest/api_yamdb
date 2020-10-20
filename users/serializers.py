from rest_framework import serializers

from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'username', 'first_name', 'last_name', 'email', 'role', 'bio',
        )
        model = CustomUser


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


class GetTokenSerializer(serializers.Serializer):
    confirmation_code = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
