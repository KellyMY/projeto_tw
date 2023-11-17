#Criação fake do banco de dados

import factory

from login.models import Login
from django.contrib.auth.models import User

class UserFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('pystr')

    class Meta:
        model = User

class LoginFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    datetime = factory.Faker('pystr')

    class Meta:
        model = Login