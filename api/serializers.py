from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Genre, Catigories, Title, Review, Comments


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("name", "slug")
        model = Genre


class CatigoriesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("name", "slug")
        model = Catigories


class TitleCreateSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field="slug",
        many=True,
    )
    category = serializers.SlugRelatedField(
        queryset=Catigories.objects.all(),
        slug_field="slug",
    )

    class Meta:
        fields = "__all__"
        model = Title


class TitleListSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    category = CatigoriesSerializer()
    rating = serializers.FloatField(read_only=True)

    class Meta:
        fields = "__all__"
        model = Title


# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = "__all__"
#         # fields = ("text", "author", "score", "pub_date",)
#         model = Review



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Review.objects.all(),
                fields=('title', 'author')
            )
        ]

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        # fields = ("text", "author", "pub_date")
        model = Comments
