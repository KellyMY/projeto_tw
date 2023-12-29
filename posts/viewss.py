from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from posts.serializers import PostsSerializer
from posts.models import Posts
# Create your views here.

@login_required(login_url='/twitter/login/')
def posts(request):
    if request.method == "GET":
        return render(request, "posts.html")
    else:
        title = request.POST.get('title')
        description = request.POST.get('description')
        user_id = request.user.id
        # return HttpResponse(user_id)
        # user
        if title and description:
            # posts = PostsSerializer
            post = Posts.objects.create_user(title=title, description=description, user_id=user_id)

            if post:
                messages.error(request, 'Campo(s) incompleto(s)! Favor preencher todos os campos.')
                return redirect("")
            else:
                messages.error(request, "Erro ao enviar a postagem!")
                return redirect("")
        else:
            messages.error(request, 'Campo(s) incompleto(s)! Favor preencher todos os campos.')
            return redirect("")