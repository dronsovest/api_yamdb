from rest_framework import serializers 

from .models import Genre, Catigories, Title


class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = "__all__"
        model = Genre


class CatigoriesSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = "__all__"
        model = Catigories


class TitleSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field="genre",
    )
    category = serializers.SlugRelatedField(
        queryset=Catigories.objects.all(),
        slug_field="category",
    )

    class Meta:
        fields = "__all__"
        model = Title
