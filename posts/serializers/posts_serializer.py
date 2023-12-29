from rest_framework import serializers
from user.models.user import User
from posts.models import Posts
# from user.serializers.user_serializer import UserSerializer

class PostsSerializer(serializers.ModelSerializer):
    # user = UserSerializer(required=True, many=True)
    # total = serializers.SerializerMethodField()

    # def get_total(self, instance):
    #     total = sum([user.username for user in instance.user.all()])
    #     return total
    # def create(self):
    #     post = Posts.objects.create_user()
    class Meta:
        model = User
        fields = ['user_code', 'total',
                  'password',
                    'email',
                    'active', 
                  ]