from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.validators import validate_email
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib.auth.decorators import login_required
from rest_framework.viewsets import ModelViewSet
from posts.models.posts import Posts
from posts.serializers.posts_serializer import PostsSerializer
from user.serializers.user_serializer import UserSerializer
from user.validation import validateEmail
from user.forms.user_form import UserForm
from user.models import User as UserModel
from follower.models import Follower

class FollowerViewSet(ModelViewSet):
    # def follow(request):
    #     return HttpResponse("Follow")
    @login_required(login_url="/twitter/login/")
    def follow(request):
        # return HttpResponse(request.POST.get("profile_id"))
        user_id_seguindo = request.POST.get("profile_id")
        user_id_seguidor = request.user.id

        follow = Follower.objects.create(follower_user_id=user_id_seguidor, following_user_id=user_id_seguindo)
        follow.save()

        messages.success(request, "Está seguindo!")
        return redirect("/twitter/profile/"+user_id_seguindo)
        # return render(request, "profile.html", )
    
    def unfollow(request):
        user_id_seguindo = request.POST.get("profile_id_un")
        user_id_seguidor = request.user.id
        # return HttpResponse(user_id_seguindo)
        unfollow = Follower.objects.get(follower_user_id=user_id_seguidor, following_user_id=user_id_seguindo)
        unfollow.delete()

        messages.success(request, "Deixou de seguir!")
        return redirect("/twitter/profile/"+user_id_seguindo)