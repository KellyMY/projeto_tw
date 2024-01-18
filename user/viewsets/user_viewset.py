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

import os
from django.conf import settings
from PIL import Image
from datetime import datetime

class UserViewSet(ModelViewSet):
       
    def index( email ):
        from django.core.validators import validate_email
        from django.core.exceptions import ValidationError
        try:
            validate_email( email )
            return True
        except ValidationError:
            return False
    
    def sign_up(request):
        # exit(request.method)
        if request.method == "GET":
            # return 'message'
            # message = request.GET.get("message")
        
            return render(request, "sign_up.html")
        else:
            # return HttpResponse('vvv')
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            password_repeat = request.POST.get("password_repeat")
            file = request.FILES.get("image")

            img = Image.open(file)
            file_string = str(file)
            file_splited = file_string.split(".")
                
            extensao = file_splited[1]

            name_image = 'image-profile-'+datetime.strftime(datetime.now(), "%Y-%m-%d_%H%M%S")+"."+extensao

            if os.path.isdir(os.path.join(settings.BASE_DIR, f'media/profile')) == False:
                os.makedirs(os.path.join(settings.BASE_DIR, f'media/profile'))
                
                
            if username and email and password and password_repeat and file:
                user = User.objects.filter(username=username).first()

                if user:
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
                    path = os.path.join(settings.BASE_DIR, f'media/profile/'+name_image)
                    img = img.save(path)
                    # file = request.FILES.get("image")
                    form_user = form.save(commit=False)
                    form_user.image = name_image
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

    def edit_profile(request):
        # exit(request.method)
        # return HttpResponse('file')
        if request.method == "GET":
            # return 'message'
            # message = request.GET.get("message")
        
            return render(request, "edit_profile.html")
        else:
            # return HttpResponse('vvv')
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            password_repeat = request.POST.get("password_repeat")
            file = request.FILES.get("image")
            # file = request.FILES.get("imagex")
            user_id = request.POST.get("user_id")
            name_image = ''
            id = ''
            img =''

            # img = Image.open(file)
            # file_string = str(file)
            # file_splited = file_string.split(".")
             
            # return HttpResponse(file)
            if file:
                img = Image.open(file)
                file_string = str(file)
                file_splited = file_string.split(".")
                    
                extensao = file_splited[1]

                name_image = 'image-profile-'+datetime.strftime(datetime.now(), "%Y-%m-%d_%H%M%S")+"."+extensao
                img = Image.open(file)

            if os.path.isdir(os.path.join(settings.BASE_DIR, f'media/profile')) == False:
                os.makedirs(os.path.join(settings.BASE_DIR, f'media/profile'))
                
                
            if username and email and password and password_repeat:
                # return HttpResponse('jjj')
                user_filter = UserModel.objects.filter(username=username)
                
                user = User.objects.filter(username=username)
                # return HttpResponse('yyy')
                user_filter.count()
                
                for u in user:
                    id = u.id
                
                if user_filter == '1' and user_id != id or user_filter == '0' and user_id != id:
                    messages.error(request, 'Nome de usuário já existe! Favor criar outro nome.')
                    return redirect('/twitter/redirect_to_edit_profile')
                        # return HttpResponse("Já existe um usuário criado!")
                    
                    # user = userx.UserRegister(request.POST)
                elif validateEmail(email) == False:
                    messages.error(request, 'E-mail incorreto! Favor digitar um e-mail.')
                    return redirect('/twitter/redirect_to_edit_profile')
                elif password != password_repeat:
                    messages.error(request, 'Senhas diferentes! Favor digitar senhas iguais.')
                    return redirect('/twitter/redirect_to_edit_profile')
                    
                # form = UserForm(request.POST)
                    # if user.is_valid():
                    #     new_user = user.save(commit=False)
                # if form.is_valid():
                    
                  
                    # file = request.FILES.get("image")
                # form_user = form.save(commit=False)
                # form.username=username
                # form.email=email
                # form.password=password

                if file:
                    path = os.path.join(settings.BASE_DIR, f'media/profile/'+name_image)
                 
                    img = img.save(path)
                    # form.image = name_image
                # user = User.objects.update(username=username, email=email, password=password)
                # user.save()
                # form.save()
                # sql_query_update = "UPDATE user_user SET username='"+str(username)+"',email='"+str(email)+"',password='"+str(password)+"' WHERE id="+str(user_id)
                
                # # return HttpResponse(sql_query_update)
                # queryset = UserModel.objects.raw(sql_query_update)
                # queryset =UserModel.objects.filter(id=user_id)
                # print(queryset)
                # xx =UserModel.objects.filter(id=user_id)
                # return HttpResponse(name_image)
                if file:
                    UserModel.objects.filter(id=user_id).update(username=username,email=email,password=password, image=name_image)
                else:
                    UserModel.objects.filter(id=user_id).update(username=username,email=email,password=password)
                
                user = User.objects.filter(id=user_id).update(username=username, email=email)
                user_u =User.objects.get(id=user_id)
                user_u.set_password(password)
                user_u.save()
                # queryset.username = username
                # # queryset.email = email
                # # queryset.password = password
                # queryset.save()
                messages.success(request, 'Usuario cadastrado com sucesso!')
                return redirect('/twitter/redirect_to_edit_profile')
                    # return HttpResponse("Usuário cadastrado com sucesso!")
            else:
                # return HttpResponse("Campo incompleto")
                messages.error(request, 'Campo(s) incompleto(s)! Favor preencher todos os campos.')
                return redirect('/twitter/redirect_to_edit_profile') 
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
                messages.error(request, 'Usuário e/ou senha inválido(s)!')
               
                return redirect("/twitter")
                # return HttpResponse("Inválido")

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
            # sql_query = "SELECT *, p.id as posts_id FROM follower_follower as f LEFT JOIN posts_posts as p ON p.user_name_id = f.following_user_id ORDER BY p.created_at DESC"
            
            # query = Posts.objects.all()
            # sql_query_user = "SELECT * from posts_posts as p LEFT JOIN user_user as u ON u.id = p.user_name_id ORDER BY p.created_at DESC"
            queryset_user = UserModel.objects.filter(id=user_id)
            # if query:
            sql_query = "SELECT * from posts_posts as p LEFT JOIN user_user as u ON u.id = p.user_name_id ORDER BY p.created_at DESC"
            queryset = Posts.objects.raw(sql_query)
            user_image = ""

            for i in queryset_user:
                user_image = ''
                user_image = "../media/profile/"+str(i.image)
            # return HttpResponse(format(settings.BASE_DIR))
            following = Follower.objects.filter(follower_user_id=user_id).count()

            follower = Follower.objects.filter(following_user_id=user_id).count()
            
            return render(request, "home.html", {"posts": queryset, "user" : user, "user_id": user_id,"user_image": user_image,"selected_name":"all", "following": following, "follower":follower})
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
        
        follower_this_profile = Follower.objects.filter(following_user_id=pk, follower_user_id=user_id)

        following = Follower.objects.filter(follower_user_id=pk).count()

        follower = Follower.objects.filter(following_user_id=pk).count()

        if follower_this_profile:
            follower_this_profile = True
        else:
            follower_this_profile = False

        if user_id == pk:
            is_user = True
        # return HttpResponse(user_id)
            
        return render(request, "profile.html", {"is_user": is_user, "profile": profile, "posts": queryset, "follow" : follower_this_profile, "follower" : follower, "following" : following})
    
    def back_login(request):
        return redirect("/twitter/login/")
    
    def back_home(request):
        return redirect("/twitter/plataform/")

    @login_required(login_url='/twitter/login/')
    def redirect_to_edit_profile(request):
        user_id = request.user.id

        user = UserModel.objects.filter(id=user_id)

        return render(request, "edit_profile.html", {"user":user, "user_id": user_id, "page_name":"EDIT PROFILE"})

    @login_required(login_url='/twitter/login/')
    def following_posts(request):
            
        count = 0
        serializer_class = PostsSerializer
        user_id = request.user.id
        
        user = request.user.username
        user_image = ''
        # selected = request.POST.get("xxxx")
        # return HttpResponse(selected)
            #following user
        queryset_user = UserModel.objects.filter(id=user_id)
            
        for i in queryset_user:
            
            user_image = "../media/profile/"+str(i.image)
            
        sql_query = "SELECT *, p.id as posts_id FROM follower_follower as f LEFT JOIN posts_posts as p ON p.user_name_id = f.following_user_id WHERE follower_user_id="+str(user_id)+" ORDER BY p.created_at DESC"
            # sql_query = "SELECT * posts_posts as p LEFT JOIN user_user as u ON u.user_name_id = p.user_name_id ORDER BY p.created_at DESC"
        queryset = Follower.objects.raw(sql_query)
       
        following = Follower.objects.filter(follower_user_id=user_id).count()

        follower = Follower.objects.filter(following_user_id=user_id).count()
        
        return render(request, "home.html", {"posts": queryset, "user" : user, "user_id": user_id, "user_image": user_image, "selected_name":"following", "following":following,"follower":follower})
    

  