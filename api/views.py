from django.db.models import Avg
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import mixins
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404

from users.permissions import IsAdmin
from .filter import TitleFilter
from .permissions import ReadOnly
from .models import Genre, Catigories, Title, Review, Comments
from .serializers import (
    GenreSerializer,
    CatigoriesSerializer,
    TitleCreateSerializer,
    TitleListSerializer,
    ReviewSerializer,
    CommentsSerializer
)


class ListCreateDeleteApiViewSet(mixins.CreateModelMixin,
                                 mixins.ListModelMixin,
                                 mixins.DestroyModelMixin,
                                 viewsets.GenericViewSet):
    pass


class GenreViewSet(ListCreateDeleteApiViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    permission_classes = (IsAdmin | ReadOnly,)
    filter_backends = [filters.SearchFilter]
    search_fields = ('name',)
    lookup_field = 'slug'


class CategoriesViewSet(ListCreateDeleteApiViewSet):
    serializer_class = CatigoriesSerializer
    queryset = Catigories.objects.all()
    permission_classes = (IsAdmin | ReadOnly,)
    filter_backends = [filters.SearchFilter]
    search_fields = ('name',)
    lookup_field = 'slug'


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(rating=Avg('title__score'))
    permission_classes = (IsAdmin | ReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filter_class = TitleFilter

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update'):
            return TitleCreateSerializer
        return TitleListSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs["title_id"])
        queryset = Review.objects.filter(title__id=self.kwargs.get("title_id"))
        return queryset


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()
    pass
