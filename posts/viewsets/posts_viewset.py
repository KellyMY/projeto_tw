from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from posts.serializers import PostsSerializer
from posts.models import Posts
from commentary.models import Commentary
# from user.models import User
from rest_framework.viewsets import ModelViewSet
from posts.forms.posts_form import PostsForm
from posts.serializers.posts_serializer import PostsSerializer
from follower.models import Follower
from datetime import datetime, timedelta

import os 
from django.conf import settings
from PIL import Image
from datetime import datetime
# Create your views here.

class PostsViewSet(ModelViewSet):
    @login_required(login_url='/twitter/login/')
    def posts(request):
        if request.method == "GET":
            # user_id = request.user.id
            
            return render(request, "posts.html")
        else:
            title = request.POST.get('title')
            description = request.POST.get('description')
            user_id = request.user.id   
            file = request.FILES.get("post_image")
            # return HttpResponse(file)

            if os.path.isdir(os.path.join(settings.BASE_DIR, f'media/post')) == False:
                os.makedirs(os.path.join(settings.BASE_DIR, f'media/post'))
            img = Image.open(file)
            file_string = str(file)
            file_splited = file_string.split(".")

            extensao = file_splited[1]
            name_image = 'image-post-'+datetime.strftime(datetime.now(), "%Y-%m-%d_%H%M%S")+"."+extensao

            

            form = PostsForm(request.POST)
            # return HttpResponse(file)
            # user
            if title and description and file:
                # return HttpResponse('uuu')
                # user = User.objects.get(id=request.user.id)
                # post_instance.user = my_p
                # return HttpResponse(form.is_valid())
                # posts = PostsSerializer
                if form.is_valid():
                    path = os.path.join(settings.BASE_DIR, f'media/post/'+name_image)
                    img = img.save(path)
                    # return HttpResponse("ttt")
                    # return HttpResponse(form.save())
                    task = form.save(commit=False)
                    # return HttpResponse(request.user)
                    task.user_name_id = request.user.id
                    task.post_image = name_image
                    # task.title = title
                    # task.description = description
                    # task.user = user_id
                    # return HttpResponse( request.user.id)
                    task.save()
                    # return HttpResponse(task.save())
                    # x = ""
                    # for u in task:
                    #     x += u+"</br>"
                    # return HttpResponse(x)
                    messages.success(request, "Postagem publicada com sucesso!")
                    return redirect("posts")
                    # return HttpResponse(f"Set is {task}")
                    # return HttpResponse(task.save())
                    # return HttpResponse(taskk)
                # post = Posts.objects.create_user(title=title, description=description, user_id=user_id)

                    # if task:
                    # messages.error(request, 'Campo(s) incompleto(s)! Favor preencher todos os campos.')
                    # return redirect("posts")
                    
                    # else:
                    #     messages.error(request, "Erro ao enviar a postagem!")
                    #     return redirect("")
                else:
                    messages.error(request, "Erro ao enviar a postagem!")
                    return redirect("posts")
            else:
                messages.error(request, 'Campo(s) incompleto(s)! Favor preencher todos os campos.')
                return redirect("posts")
            
    def publication(request, pk):
        # post = Posts.objects.filter(id=pk)
        user_id = request.user.id
        sql_query = "SELECT * FROM posts_posts p LEFT JOIN user_user as u ON u.id = p.user_name_id WHERE p.id="+str(pk)
        post = Posts.objects.raw(sql_query)
        user_id_in_post = 0

        for p in post:
            user_id_in_post = p.user_name_id


        # sql_query_commentary = "SELECT *,DATE_FORMAT(c.date_commentary,'%Y-%m-%d %H:%i:%s') as date_commentary FROM commentary_commentary as c LEFT JOIN user_user as u ON u.id = c.user_name_commentary_id LEFT JOIN posts_posts as p ON p.id = c.post_id WHERE c.post_id="+str(pk)
        sql_query_commentary = "SELECT * FROM commentary_commentary as c LEFT JOIN user_user as u ON u.id = c.user_name_commentary_id LEFT JOIN posts_posts as p ON p.id = c.post_id WHERE c.post_id="+str(pk)+" ORDER BY c.date_commentary DESC"
        commentary = Commentary.objects.raw(sql_query_commentary)

        following = Follower.objects.filter(follower_user_id=user_id_in_post).count()

        follower = Follower.objects.filter(following_user_id=user_id_in_post).count()
        # return HttpResponse(follower)
        is_user = False
        user_of_post = 0
        follower_this_profile = False
        i = 0

        for p in post:
            user_of_post = p.user_name_id

            if p.user_name_id == request.user.id:
                is_user = True

        for c in commentary:
            format_datetime = datetime.now()
            
            date_commentary = datetime.strftime(c.date_commentary,"%Y/%m/%d %H:%M:%S")
            datetime_now = format_datetime.strftime("%Y/%m/%d %H:%M:%S")
            # return HttpResponse(datetime_now)
            date_commentary = datetime.strptime(str(date_commentary),"%Y/%m/%d %H:%M:%S")
            data_em_texto = datetime.strptime(str(datetime_now),"%Y/%m/%d %H:%M:%S")
            # return HttpResponse(data_em_texto)
            # end_date = datetime.datetime.utcnow()
            # start_date = end_date - datetime.timedelta(days=8)
            # difference_in_days = abs((end_date - start_date).days)
            
            # str_d1 = '2021/10/20 10:20:00'
            # str_d2 = '2022/2/20 11:20:00'

            # # convert string to date object
            # d1 = datetime.strptime(str_d1, "%Y/%m/%d %H:%M:%S")
            # d2 = datetime.strptime(str_d2, "%Y/%m/%d %H:%M:%S")

            # # difference between dates in timedelta
            # delta = d2 - d1
            d = data_em_texto - date_commentary
            # print(f'Difference is {d.seconds//3600} hours')
            # print(f'Difference is {d.seconds//60} minutes')
            # print(f'Difference is {d.seconds//3600} seconds')
            # return HttpResponse(d.seconds//360000)
            # return HttpResponse(d.time)
            # if(diferenca_datas < 24):
            #     print('kkk')
            
            commentary[i].date_diferenca_hours = d.seconds//3600
            commentary[i].date_diferenca_minutes = d.seconds//60
            commentary[i].date_diferenca_seconds = d.seconds
            i+=1
                


        follower_this_profile = Follower.objects.filter(following_user_id=user_of_post, follower_user_id=request.user.id)

        sql_query_user = "SELECT * from posts_posts as p LEFT JOIN user_user as u ON u.id = p.user_name_id ORDER BY p.created_at DESC"
        queryset_user = Posts.objects.raw(sql_query_user)
        user_image = ""

        for i in queryset_user:
            user_image = ''
            user_image = "../media/profile/"+str(i.image)

        if follower_this_profile:
            follower_this_profile = True
        else:
            follower_this_profile = False

       
        # user=post[0]["user_name"]["user_name_id"]
        # user = 0
        # user = post.select_related("user_name")
        # return HttpResponse(user)
        # return redirect("/twitter/publication")
        # return HttpResponse(is_user)
        return render(request, "publication.html", {"post": post, "is_user": is_user, "user_id":user_id,"user_image":user_image, "follow":follower_this_profile, "following": following, "follower": follower, "commentary":commentary})
    
    def back_published(request):
        return redirect("/twitter/plataform/")