from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from posts.models import Posts
# from user.models import User
from rest_framework.viewsets import ModelViewSet
from posts.forms.posts_form import PostsForm
from posts.serializers.posts_serializer import PostsSerializer
from follower.models import Follower
from commentary.models import Commentary
from commentary.forms import CommentaryForm

class CommentaryViewSet(ModelViewSet):
    @login_required(login_url='/twitter/login/')
    def comment(request):
        if request.method == "POST":
            user_id = request.user.id
            comment = request.POST.get("comment")
            post_id = request.POST.get("post_id")

            form = CommentaryForm(request.POST)
            # return HttpResponse(form.is_valid())
            # return HttpResponse(post_id)
            if comment:
                if form.is_valid():
                    task = form.save(commit=False)
                    task.user_name_commentary_id = user_id
                    task.post_id = post_id
                    # for i in task:
                    #     print(i)
                    # return HttpResponse(post_id)
                    task.save()

                    messages.success(request, "Comentário salvo com sucesso!")
                    return redirect("/twitter/publication/%s"%post_id)
                else:
                    messages.error(request, "Erro ao salvar o comentário!")
                    return redirect("/twitter/publication/%s"%post_id)
            else:
                messages.error(request, "Campo incompleto!")
                return redirect("/twitter/publication/%s"%post_id)
        else:
            return HttpResponse("dddd")