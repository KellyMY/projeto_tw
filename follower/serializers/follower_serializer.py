from rest_framework import serializers
from user.models import User
from user.serializers.user_serializer import UserSerializer

class FollowerSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True, many=True)
    total = serializers.SerializerMethodField()

    def get_total(self, instance):
        total = sum([user.username for user in instance.user.all()])
        return total
    
    class Meta:
        model = User
        fields = ['username', 'total',
                  ]