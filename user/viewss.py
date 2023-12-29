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
# from user.models import *
# Create your views here.

def index(request):
    current_user = request.GET.get("user")
def sign_up(request):
    # exit(request.method)
    if request.method == "GET":
        # return 'message'
        # message = request.GET.get("message")
       
        return render(request, "sign_up.html", )
    else:
        # return HttpResponse('vvv')
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_repeat = request.POST.get("password_repeat")
        
        if username and email and password and password_repeat:
            user = User.objects.filter(username=username).first()
            if user:

                # messages.info(request,"Existe")
                messages.error(request, 'Nome de usuário já existe! Favor criar outro nome.')
                return redirect('sign_up')
                # return HttpResponse("Já existe um usuário criado!")
            
            # user = userx.UserRegister(request.POST)
            elif validateEmail(email) == False:
                messages.error(request, 'E-mail incorreto! Favor digitar um e-mail.')
                return redirect('sign_up')
            elif password != password_repeat:
                messages.error(request, 'Senhas diferentes! Favor digitar senhas iguais.')
                return redirect('sign_up')
            
            # if user.is_valid():
            #     new_user = user.save(commit=False)
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Usuario cadastrado com sucesso!')
            return redirect('sign_up')
            # return HttpResponse("Usuário cadastrado com sucesso!")
        else:
            # return HttpResponse("Campo incompleto")
            messages.error(request, 'Campo(s) incompleto(s)! Favor preencher todos os campos.')
            return redirect('sign_up') 
            # return HttpResponse(messages.error(request, "campos incomepltos"))
            # return render(request,"", {'message' : 'Campo(s) incompleto!'})

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            login_django(request, user)

            return redirect("/plataform/")
            # return HttpResponse("autenticado")
        else:
            return HttpResponse("Inválido")

def logout(request):
    logout_django(request)
    return redirect("/login/")

@login_required(login_url='/twitter/login/') 
def plataform(request):
    serializer_class = PostsSerializer
    # queryset = PostsSerializer
    # return HttpResponse(queryset)
    # if queryset:
    user_id = request.user.id
    user = request.user.username
    queryset = Posts.objects.all().order_by('id')  #filter()s
    # return HttpResponse(user)
    # if registers:
        # registers = Posts.objects.filter(username=u)
    # path("plataform/", views.plataform, name="plataform"),
    # return render(request, "plataform")
    return render(request, "home.html", {"posts": queryset, "user" : user, "user_id": user_id})
    # if request.user.is_authenticated:
        # return HttpResponse("plataform")
    
    # return HttpResposnse("Faça login primeiro!")

def button_sign_up(request):
    return redirect("/sign_up/")

def validateEmail( email ):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email( email )
        return True
    except ValidationError:
        return False