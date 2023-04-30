from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    APIGetToken,
    APISignup,
    CategoriesViewSet,
    CommentViewSet,
    GenreViewSet,
    ReviewViewSet,
    TitlesViewSet,
    UsersViewSet,
)

app_name = "api"

v1_router = DefaultRouter()
v1_router.register("users", UsersViewSet, basename="users")
v1_router.register("categories", CategoriesViewSet, basename="categories")
v1_router.register("genres", GenreViewSet, basename="genres")
v1_router.register("titles", TitlesViewSet, basename="titles")
v1_router.register(
    r"titles/(?P<title_id>\d+)/reviews", ReviewViewSet, basename="reviews"
)
v1_router.register(
    r"titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments",
    CommentViewSet,
    basename="review_comments",
)

urlpatterns = [
    path("v1/auth/token/", APIGetToken.as_view(), name="get_token"),
    path("v1/", include(v1_router.urls)),
    path("v1/auth/signup/", APISignup.as_view(), name="signup"),
]
