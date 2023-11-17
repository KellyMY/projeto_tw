from rest_framework.viewsets import ModelViewSet
from postagem.serializers.postagem_serializer import PostagemSerializer
from postagem.models import Postagem

class PostagemViewSet(ModelViewSet):
    serializer_class = PostagemSerializer
    
    def get_queryset(self):
        return Postagem.objects.all().order_by("id")