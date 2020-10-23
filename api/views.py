from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import Genre, Catigories, Title
from .serializers import (
    GenreSerializer,
    CatigoriesSerializer,
    TitleSerializer,
)


class IsSuperuserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class GenreViewSet(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    permissions = (IsSuperuserPermission,)


class CategoriesViewSet(viewsets.ModelViewSet):
    serializer_class = CatigoriesSerializer
    queryset = Catigories.objects.all()
    permissions = (IsSuperuserPermission,)



class TitleViewSet(viewsets.ModelViewSet):
    serializer_class = TitleSerializer
    queryset = Title.objects.all()
    permissions = (IsSuperuserPermission,)
