from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsSuperuserPermission
from .models import Genre, Catigories, Title
from .serializers import (
    GenreSerializer,
    CatigoriesSerializer,
    TitleSerializer,
)


class GenreViewSet(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    pagination_class = PageNumberPagination
    permission_classes = (IsSuperuserPermission, )
    filter_backends = [filters.SearchFilter]
    search_fields = ('name', )
    lookup_field = 'slug'


class CategoriesViewSet(viewsets.ModelViewSet):
    serializer_class = CatigoriesSerializer
    queryset = Catigories.objects.all()
    pagination_class = PageNumberPagination
    permission_classes = (IsSuperuserPermission,)
    filter_backends = [filters.SearchFilter]
    search_fields = ('name',)
    lookup_field = 'slug'


class TitleViewSet(viewsets.ModelViewSet):
    serializer_class = TitleSerializer
    queryset = Title.objects.all()
    pagination_class = PageNumberPagination
    permission_classes = (IsSuperuserPermission,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_fields = ('category', 'genre')
    search_fields = ('name', 'year')
    lookup_field = 'slug'
