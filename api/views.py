from django.db.models import Avg
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import mixins
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from requests import Response

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


# class ReviewViewSet(ListCreateDeleteApiViewSet):
#     serializer_class = ReviewSerializer
#
#     @permission_classes([IsAuthenticated])
#     def get_queryset(self):
#         title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
#         queryset = Review.objects.filter(title__id=self.kwargs.get('title_id'))
#         return queryset

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = [IsAdmin]
    # pagination_class = PageNumberPagination
    # @permission_classes([IsAuthenticated])
    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs["title_id"])
        queryset = Review.objects.filter(title__id=self.kwargs.get('title_id'))
        return queryset

    @permission_classes([IsAuthenticated])
    def create(self, serializer, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        # title = get_object_or_404(Title, pk=self.kwargs["title_id"])
        serializer.is_valid(raise_exception=True)
        title_id = self.kwargs.get("title_id")
        title = get_object_or_404(Title, pk=title_id)
        serializer.save(author=self.request.user, title=title)
        return serializer.data
        # serializer.save(author=self.request.user)

    # #
    # @permission_classes([IsAuthenticated])
    # def perform_create(self, serializer):
    #     serializer.save()
    # @permission_classes([IsAuthenticated])
    # def create(self, serializer, *args, **kwargs):
    #     serializer = self.get_serializer(data=self.request.data)
    #     serializer.is_valid(raise_exception=True)
    #     title_id = self.kwargs.get("title_id")
    #     title = get_object_or_404(Title, pk=title_id)
    #     if Review.objects.all().filter(title=title, author=self.request.user).count() == 1:
    #         headers = self.get_success_headers(serializer.validated_data)
    #         return Response(status=400, headers=headers)
    #     serializer.save(author=self.request.user, title=title)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=201, headers=headers)

    # @permission_classes([IsAdmin])
    # @permission_classes([IsAuthenticated])
    # def (self)
class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()

    @permission_classes([ReadOnly])
    def get_queryset(self):
        review = get_object_or_404(Comments, id=self.kwargs.get('review_id'))
        queryset = Comments.objects.filter(title__id=self.kwargs.get('review_id'))
        return queryset
