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

class UserViewSet(ModelViewSet):
       
    def index( email ):
        from django.core.validators import validate_email
        from django.core.exceptions import ValidationError
        try:
            validate_email( email )
            return True
        except ValidationError:
            return False
    # def index(request):
    #     current_user = request.GET.get("user")

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
                    return redirect('/twitter/sign_up')
                    # return HttpResponse("Já existe um usuário criado!")
                
                # user = userx.UserRegister(request.POST)
                elif validateEmail(email) == False:
                    messages.error(request, 'E-mail incorreto! Favor digitar um e-mail.')
                    return redirect('/twitter/sign_up')
                elif password != password_repeat:
                    messages.error(request, 'Senhas diferentes! Favor digitar senhas iguais.')
                    return redirect('/twitter/sign_up')
                
                form = UserForm(request.POST)
                # if user.is_valid():
                #     new_user = user.save(commit=False)
                if form.is_valid():
                    form_user = form.save(commit=False)
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    form_user.save()

                    messages.success(request, 'Usuario cadastrado com sucesso!')
                    return redirect('/twitter/sign_up')
                # return HttpResponse("Usuário cadastrado com sucesso!")
            else:
                # return HttpResponse("Campo incompleto")
                messages.error(request, 'Campo(s) incompleto(s)! Favor preencher todos os campos.')
                return redirect('/twitter/sign_up') 
                # return HttpResponse(messages.error(request, "campos incomepltos"))
                # return render(request,"", {'message' : 'Campo(s) incompleto!'})

    def login(request):
        if request.method == "GET":
            return render(request, "login.html")
        else:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user_id = request.user.id
            user = authenticate(username=username, password=password)

            if user:
                login_django(request, user)

                return redirect("/twitter/plataform/")
                # return HttpResponse("autenticado")
            else:
                return HttpResponse("Inválido")

    def logout(request):
        logout_django(request)
        return redirect("/twitter/login/")

    @login_required(login_url='/twitter/login/') 
    def plataform(request):
        try:
            count = 0
            serializer_class = PostsSerializer
                # queryset = PostsSerializer
                # return HttpResponse(queryset)
                # if queryset:
            user_id = request.user.id
            # return HttpResponse(user_id)
            user = request.user.username
            # queryset = ""
            # queryset = Posts.objects.filter(user_name_id=user_id)  #filter()s
            # followings = Follower.objects.filter(follower_user_id=user_id)
            # followings_ids = []
            # followings_ids = ""
            # variable_or = ''
            sql_query = "SELECT *, p.id as posts_id FROM follower_follower as f LEFT JOIN posts_posts as p ON p.user_name_id = f.following_user_id ORDER BY p.created_at DESC"
            queryset = Follower.objects.raw(sql_query)

            # for i in queryset:
            #     count += 1
            # if followings:
            #     for following in followings:
            #         # for f in following:
            #             # return HttpResponse(following.following_user_id)
            #             # followings_ids += variable_or + "user_name_id="+str(following.following_user_id)
            #             # followings_ids.append(following.follower_user_id)
            #             # variable_or = " | "
            #             ds = Posts.objects.filter(user_name_id=following.following_user_id)
            #             if ds:
            #                 for d in ds:
            #                     queryset.update(d)
            #             # return HttpResponse(following)

            # if followings_ids:
            #     for following_id in followings_ids:
            # return HttpResponse(followings_ids)
            # queryset = Posts.objects.filter((int(followings_ids)))
            # return HttpResponse(queryset)
            # return HttpResponse(queryset)
            # queryset = Follower.objects.filter(follower_user_id=user_id).prefetch_related("toppings").all()
            # queryset = Follower.objects.aggregate(user=Posts("user_name")).filter(follower_user_id=user_id)
            # return HttpResponse(queryset)
            # queryset = Posts.objects.all()
        # if queryset:
            # return HttpResponse(queryset)
            # if registers:
                # registers = Posts.objects.filter(username=u)
            # path("plataform/", views.plataform, name="plataform"),
            # return render(request, "plataform")
            # messages.error(request, 'Campo(s) incompleto(s)! Favor preencher todos os campos.')
            # return redirect('home') 
            # return HttpResponse(count)
            return render(request, "home.html", {"posts": queryset, "user" : user, "user_id": user_id})
        except Posts.DoesNotExist:
            messages.error(request, 'Nenhuma postagem.')
            # return redirect('') 
            return render(request, "home.html")
        # if request.user.is_authenticated:
            # return HttpResponse("plataform")
        
        # return HttpResposnse("Faça login primeiro!")

    def button_sign_up(request):
        return redirect("/twitter/sign_up/")

    @login_required(login_url='/twitter/login/')
    def profile(request, pk):
        is_user = False
        # serializer_class = FollowSerializer
        # return HttpResponse(pk)
        profile = UserModel.objects.filter(id=pk)

        queryset = Posts.objects.filter(user_name_id=pk)
        # return HttpResponse(profile)
        user_id = request.user.id
        # return HttpResponse(user_id)
# follower_user
# following_user
        follower_this_profile = Follower.objects.filter(following_user_id=pk, follower_user_id=user_id)

        following = Follower.objects.filter(follower_user_id=pk).count()

        follower = Follower.objects.filter(following_user_id=pk).count()

        if follower_this_profile:
            follower_this_profile = True
        else:
            follower_this_profile = False

        if user_id == pk:
            is_user = True
        # return HttpResponse(follower_this_profile)
        return render(request, "profile.html", {"is_user": is_user, "profile": profile, "posts": queryset, "follow" : follower_this_profile, "follower" : follower, "following" : following})
  