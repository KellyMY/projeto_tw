from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# from user.

# Create your views here.
@login_required(login_url="/twitter/login/")
def follower(request):
    user_id = request.user.id
    user = request.user.username
    # return HttpResponse("ddddd")
    return render(request, "follower.html", {"user_id": user_id, "user": user})

def unfollow(request):
    return HttpResponse('gggg')