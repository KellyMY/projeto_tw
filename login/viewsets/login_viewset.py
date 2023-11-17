from rest_framework.viewsets import ModelViewSet
from login.serializers.login_serializer import LoginSerializer
from login.models import Login

class LoginViewSet(ModelViewSet):
    serializer_class = LoginSerializer
    
    def get_queryset(self):
        return Login.objects.all().order_by("id")