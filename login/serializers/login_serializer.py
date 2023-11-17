from rest_framework import serializers
from login.models import Login
from login.serializers.login_serializer import LoginSerializer

class LoginSerializer(serializers.ModelSerializer):
    login = LoginSerializer(required=True, many=True)
    total = serializers.SerializerMethodField()

    def get_total(self, instance):
        total = sum([login.user for login in instance.login.all()])
        return total
    
    class Meta:
        model = Login
        fields = ['user', 'datetime']
