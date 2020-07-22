from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User
from account.models import Follower

def homePage(request) : 
    if request.user.is_authenticated : 
        return render(request, 'pages/home.html')
    else : 
        return render(request, 'pages/index.html')

def viewUser(request, username) :
    username = username.split("@")[0]
    if User.objects.filter(username=username).exists() : 
        user = User.objects.get(username=username)
        following = Follower.objects.filter(user_from__username=username)
        followers = Follower.objects.filter(user_to__username=username)

        if request.user.is_authenticated : 
            follow_status = True if Follower.objects.filter(user_from=request.user, user_to__username=username).exists() else False
        else :
            follow_status = False
    
        return render(request, 'pages/userprofile.html', {"user_data" : user, "following": following, "followers" : followers, "status" : follow_status})
    else : 
        raise Http404()

    