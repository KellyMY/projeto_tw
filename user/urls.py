from rest_framework import routers
from django.urls import path
# from . import viewss as views
from posts.viewsets import PostsViewSet as views_posts
from follower.viewsets import FollowerViewSet as followers
from user import viewsets
from commentary.viewsets import CommentaryViewSet as views_commentary
from django.conf import settings
from django.conf.urls.static import static

router = routers.SimpleRouter()
router.register(r'user', viewsets.UserViewSet, basename='user')

urlpatterns = [
    path("sign_up/", viewsets.UserViewSet.sign_up, name="sign_up"),
    path("login/", viewsets.UserViewSet.login, name="login"),
    path("logout/", viewsets.UserViewSet.logout, name="logout"),
    path("redirect_to_edit_profile/", viewsets.UserViewSet.redirect_to_edit_profile, name="redirect_to_edit_profile"),
    path("edit_profile/", viewsets.UserViewSet.edit_profile, name="edit_profile"),
    path("plataform/", viewsets.UserViewSet.plataform, name="plataform"),
    path("profile/<int:pk>", viewsets.UserViewSet.profile, name="profile"),
    path("posts/", views_posts.posts, name="posts"),
    path("follow/", followers.follow, name="follow"),
    path("button_sign_up/", viewsets.UserViewSet.button_sign_up, name="button_sign_up"),
    path("publication/<int:pk>", views_posts.publication, name="publication"),
    path("unfollow", followers.unfollow, name="unfollow"),
    
    path("back_published/", views_posts.back_published, name="back_published"),
    path("following_posts/", viewsets.UserViewSet.following_posts, name="following_posts"),
    
    path("back_login/", viewsets.UserViewSet.back_login, name="back_login"),
    path("back_home/", viewsets.UserViewSet.back_home, name="back_home"),
    
    path("comment/", views_commentary.comment, name="comment"),
    # path("comment/", viewsets.UserViewSet.comment, name="comment"),
    # path("comment/", views_comment.comment, name="comment"),
    path("", viewsets.UserViewSet.login, name="login"),

   
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)