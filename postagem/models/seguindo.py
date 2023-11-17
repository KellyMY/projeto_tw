from django.db import models
from django.contrib.auth.models import User

class Seguindo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_following = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.user