from django.db import models
from django.contrib.auth.models import User

class Postagem(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=200, blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title
