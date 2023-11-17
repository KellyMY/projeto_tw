from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    active = models.BooleanField(default=True)


    # titulo = models.CharField(max_length=250)
    # descricao = models.CharField(max_length=200, blank=True, null=True)
    # data = models.CharField(max_length=50)
    # active = models.BooleanField(default=True)
    # #  product = models.ManyToManyField(Product, blank=False)
    # user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __unicode__(self):
        return self.titulo