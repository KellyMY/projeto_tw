from django.db import models
from django.contrib.auth.models import User

class Login(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.nome