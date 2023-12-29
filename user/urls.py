from rest_framework import routers
from django.urls import path
# from . import viewss as views
from posts.viewsets import PostsViewSet as views_posts
from follower.viewsets import FollowerViewSet as followers
from user import viewsets

router = routers.SimpleRouter()
router.register(r'user', viewsets.UserViewSet, basename='user')

urlpatterns = [
    path("sign_up/", viewsets.UserViewSet.sign_up, name="sign_up"),
    path("login/", viewsets.UserViewSet.login, name="login"),
    path("logout/", viewsets.UserViewSet.logout, name="logout"),
    path("plataform/", viewsets.UserViewSet.plataform, name="plataform"),
    path("profile/<int:pk>", viewsets.UserViewSet.profile, name="profile"),
    path("posts/", views_posts.posts, name="posts"),
    path("follow/", followers.follow, name="follow"),
    path("button_sign_up/", viewsets.UserViewSet.button_sign_up, name="button_sign_up"),
    path("publication/<int:pk>", views_posts.publication, name="publication"),
    path("unfollow", followers.unfollow, name="unfollow"),
    
    path("", viewsets.UserViewSet.login, name="login"),
]