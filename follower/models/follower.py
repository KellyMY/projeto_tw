from django.db import models
# from django.contrib.auth.models import User
from user.models import User
from posts.models import Posts
# from user.models.user import User as userdata

class Follower(models.Model):
    follower_user = models.ForeignKey(User, null=False, blank=True, default=None, on_delete=models.CASCADE, related_name="follower_user")

    following_user = models.ForeignKey(User, null=False, blank=True, default=None, on_delete=models.CASCADE, related_name="following_user")

# class Follower(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     user_following = models.ManyToManyField(User, blank=True)
    # user_following = models.CharField(max_length=150)
    # user = models.CharField(max_length=150)
    