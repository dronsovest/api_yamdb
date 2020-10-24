from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .permissions import IsSuperuserPermission
from .models import Genre, Catigories, Title
from .serializers import (
    GenreSerializer,
    CatigoriesSerializer,
    TitleSerializer,
)
#from rest_framework import permissions

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 5


class GenreViewSet(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    pagination_class = StandardResultsSetPagination
    permission_classes = (IsSuperuserPermission, )


class CategoriesViewSet(viewsets.ModelViewSet):
    serializer_class = CatigoriesSerializer
    queryset = Catigories.objects.all()
    pagination_class = StandardResultsSetPagination
    permission_classes = (IsSuperuserPermission,)


class TitleViewSet(viewsets.ModelViewSet):
    serializer_class = TitleSerializer
    queryset = Title.objects.all()
    pagination_class = StandardResultsSetPagination
    permission_classes = (IsSuperuserPermission,)
