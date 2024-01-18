from django.db import models
from user.models import User
from django.conf import settings

class Posts(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    user_name = models.ForeignKey(User, null=False, blank=True, default=None, on_delete=models.CASCADE, related_name="usernames")
    # user_code = models.OneToOneField(User, on_delete=models.CASCADE)
    #   user = models.ForeignKey(User,on_delete=models.CASCADE)
    # user = models.ManyToManyField(User, blank=True)
    title = models.CharField(max_length=1500)
    description = models.CharField(max_length=1500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # email = models.CharField(max_length=200)
    post_image = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

