from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from rest_framework import mixins
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsSuperuserPermission
from .models import Genre, Catigories, Title
from .serializers import (
    GenreSerializer,
    CatigoriesSerializer,
    TitleSerializer,
)


class ListCreateApiViewSet(mixins.CreateModelMixin, 
                           mixins.ListModelMixin, 
                           viewsets.GenericViewSet): 
    pass 


class GenreViewSet(ListCreateApiViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    pagination_class = PageNumberPagination
    permission_classes = (IsSuperuserPermission, )
    filter_backends = [filters.SearchFilter]
    search_fields = ('name', )
    lookup_field = 'slug'


class CategoriesViewSet(ListCreateApiViewSet):
    serializer_class = CatigoriesSerializer
    queryset = Catigories.objects.all()
    pagination_class = PageNumberPagination
    permission_classes = (IsSuperuserPermission,)
    filter_backends = [filters.SearchFilter]
    search_fields = ('name',)
    lookup_field = 'slug'

    def perform_destroy(self, serializer):
        serializer.delete()


class TitleViewSet(viewsets.ModelViewSet):
    serializer_class = TitleSerializer
    queryset = Title.objects.all()
    pagination_class = PageNumberPagination
    permission_classes = (IsSuperuserPermission,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_fields = ('category', 'genre')
    search_fields = ('name', 'year')
    lookup_field = 'slug'
