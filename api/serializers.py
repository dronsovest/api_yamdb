from rest_framework import serializers

from .models import Genre, Catigories, Title


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("name", "slug")
        model = Genre


class CatigoriesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("name", "slug")
        model = Catigories


class TitleSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field="slug",
        many=True,
    )
    category = serializers.SlugRelatedField(
        queryset=Catigories.objects.all(),
        slug_field="slug",
        required=False,
    )

    year = serializers.IntegerField(required=False)

    class Meta:
        fields = ('id', 'name', 'year', 'description', 'genre', 'category')
        model = Title
        # extra_kwargs = {'year': {'required': False}}
