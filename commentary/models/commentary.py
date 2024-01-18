from django.db import models
from user.models import User
from posts.models import Posts
from datetime import datetime
from django.utils import timezone

class Commentary(models.Model):
    user_name_commentary = models.ForeignKey(User, null=False, blank=True, default=None, on_delete=models.CASCADE, related_name="usernamescommentary")
    post = models.ForeignKey(Posts, null=False, blank=True, default=None, on_delete=models.CASCADE, related_name="posts")
    comment = models.CharField(max_length=1500)
    date_commentary = models.DateTimeField(default=timezone.now)