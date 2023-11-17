from rest_framework import serializers
from usuario.models.usuario import Usuario
# from usuario.serializers.usuario_serializer import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'name',
            'email',
            'phone',
            'active',
        ]

        # extra_kwargs = {}