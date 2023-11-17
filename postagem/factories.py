#Criação fake do banco de dados
import factory

from postagem.models import Postagem
from django.contrib.auth.models import User

class UserFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('pystr')

    class Meta:
        model = User

class PostagemFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    
    title = factory.Faker("pystr")
    description = factory.Faker("pystr")
    datetime = factory.Faker("pystr")
    active = factory.Faker("pystr")

    class Meta:
        model = Postagem