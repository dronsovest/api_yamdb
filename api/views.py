from django.db.models import Avg
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from users.permissions import IsAdmin

from .filter import TitleFilter
from .models import Catigories, Comments, Genre, Review, Title
from .permissions import IsModerator, IsOwner, ReadOnly
from .serializers import (CatigoriesSerializer, CommentsSerializer,
                          GenreSerializer, ReviewSerializer,
                          TitleCreateSerializer, TitleListSerializer)


class ListCreateDeleteApiViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    pass


class GenreViewSet(ListCreateDeleteApiViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    permission_classes = (IsAdmin | ReadOnly,)
    filter_backends = [filters.SearchFilter]
    search_fields = ("name",)
    lookup_field = "slug"


class CategoriesViewSet(ListCreateDeleteApiViewSet):
    serializer_class = CatigoriesSerializer
    queryset = Catigories.objects.all()
    permission_classes = (IsAdmin | ReadOnly,)
    filter_backends = [filters.SearchFilter]
    search_fields = ("name",)
    lookup_field = "slug"


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(rating=Avg("title__score"))
    permission_classes = (IsAdmin | ReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filter_class = TitleFilter

    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update"):
            return TitleCreateSerializer
        return TitleListSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsOwner | ReadOnly | IsModerator | IsAdmin,)

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs["title_id"])
        return title.title.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs["title_id"])
        if Review.objects.filter(
                author=self.request.user,
                title_id=title
        ).exists():
            raise ValidationError(
                detail="Добавить больше одного обзора нельзя"
            )
        serializer.save(author=self.request.user, title=title)

    """метод PATCH пока не работает, отдаёт 404 почему-то"""
    def partial_update(self, request, pk=None, title_id=None):
        review = get_object_or_404(
            Review,
            title_id=self.kwargs.get("title_id"),
            pk=self.kwargs.get("review_id"),
        )
        serializer = ReviewSerializer(
            review,
            data=self.request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=404)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()
    permission_classes = (IsOwner | ReadOnly | IsModerator | IsAdmin,)

    def get_queryset(self):
        review = get_object_or_404(
            Review,
            pk=self.kwargs.get("review_id"),
            title_id=self.kwargs.get("title_id"),
        )
        return review.review.all()

    def perform_create(self, serializer):
        review = get_object_or_404(
            Review,
            pk=self.kwargs.get("review_id"),
            title_id=self.kwargs.get("title_id"),
        )
        serializer.save(author=self.request.user, review=review)

    """метод PATCH пока не работает, отдаёт 404 почему-то"""
    def partial_update(self, request, pk=None, title_id=None, review_id=None):
        comment = get_object_or_404(
            Comments,
            pk=self.kwargs.get("comments_id"),
            title_id=self.kwargs.get("title_id"),
            review_id=self.kwargs.get("review_id"),
        )
        serializer = CommentsSerializer(
            comment,
            data=self.request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=200)
        return Response(data=serializer.errors, status=404)
