from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from .views import GenreViewSet, CategoriesViewSet, TitleViewSet

from users.views import GetConfirmationCode, GetToken, UserViewSet

router = DefaultRouter()

router.register('users', UserViewSet, basename='users')
router.register('genres', GenreViewSet, basename='genres')
router.register('categories', CategoriesViewSet, basename='categories')
router.register('titles', TitleViewSet, basename='titles')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/email/', GetConfirmationCode.as_view()),
    path('v1/auth/token/', GetToken.as_view()),
]
