#Criação fake do banco de dados

import factory
from usuario.models import Usuario

class UsuarioFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("pystr")
    email = factory.Faker("pystr")
    phone = factory.Faker("pystr")
    active = factory.Iterator([True, False])

    class Meta:
        model = Usuario

