from rest_framework import serializers

from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'username', 'first_name', 'last_name', 'email', 'role', 'bio',
        )
        model = CustomUser


class EmailSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = CustomUser
        fields = ('email',)


class GetTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    confirmation_code = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = ('email', 'confirmation_code',)
