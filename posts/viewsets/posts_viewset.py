from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from posts.serializers import PostsSerializer
from posts.models import Posts
# from user.models import User
from rest_framework.viewsets import ModelViewSet
from posts.forms.posts_form import PostsForm
from posts.serializers.posts_serializer import PostsSerializer
from follower.models import Follower
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

            form = PostsForm(request.POST)
            # return HttpResponse(user_id)
            # user
            if title and description:
                # return HttpResponse('uuu')
                # user = User.objects.get(id=request.user.id)
                # post_instance.user = my_p
                # return HttpResponse(form.is_valid())
                # posts = PostsSerializer
                if form.is_valid():
                    # return HttpResponse("ttt")
                    # return HttpResponse(form.save())
                    task = form.save(commit=False)
                    # return HttpResponse(request.user)
                    task.user_name_id = request.user.id
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
        
        sql_query = "SELECT * FROM posts_posts p LEFT JOIN user_user as u ON u.id = p.user_name_id WHERE p.id="+str(pk)
        post = Posts.objects.raw(sql_query)

        is_user = False
        user_of_post = 0
        follower_this_profile = False

        for p in post:
            user_of_post = p.user_name_id

            if p.user_name_id == request.user.id:
                is_user = True

            

        follower_this_profile = Follower.objects.filter(following_user_id=user_of_post, follower_user_id=request.user.id)

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
        return render(request, "publication.html", {"post": post, "is_user": is_user, "follow":follower_this_profile})