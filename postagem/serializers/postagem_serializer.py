from rest_framework import serializers
from postagem.models.postagem import Postagem
from usuario.models.usuario import Usuario
from usuario.serializers.usuario_serializer import UsuarioSerializer

class PostagemSerializer(serializers.ModelSerializer):
    user = UsuarioSerializer(read_only=True, many=True)

    class Meta:
        model = Postagem
        fields = [
            'title',
            'description',
            'datetime',
            'active',
            'user',
        ]

        extra_kwargs = {'desccription': {'required' : False}}

    # def create(self, validated_data):
    #     user_data = validated_data.pop('user')

    #     user = Usuario.objects.create(**validated_data)

    #     for u in user_data:
    #         u.usuario