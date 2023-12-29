from rest_framework import serializers
from user.models import User
# from user.serializers.user_serializer import UserSerializer

class UserSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    # class Meta:
    #     model = 