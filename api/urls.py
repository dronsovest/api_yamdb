from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from .views import GenreViewSet, CategoriesViewSet, TitleViewSet, ReviewViewSet, CommentViewSet

from users.views import GetConfirmationCode, GetToken, UserViewSet

router = DefaultRouter()

router.register("users", UserViewSet, basename="users")
router.register("genres", GenreViewSet, basename="genres")
router.register("categories", CategoriesViewSet, basename="categories")
router.register("titles", TitleViewSet, basename="titles")
router.register(r"titles/(?P<title_id>\d+)/reviews", ReviewViewSet, basename="reviews")
router.register(r"titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments", CommentViewSet, basename="comments")

urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/auth/email/", GetConfirmationCode.as_view()),
    path("v1/auth/token/", GetToken.as_view()),
]
