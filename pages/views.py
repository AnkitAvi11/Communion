from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User
from django.core.serializers import serialize

def homePage(request) : 
    if request.user.is_authenticated : 
        return render(request, 'pages/home.html')
    else : 
        return render(request, 'pages/index.html')

def viewUser(request, username) :
    username = username.split("@")[0]
    if User.objects.filter(username=username).exists() : 
        user = serialize("json", User.objects.filter(username=username))
        return JsonResponse(user, safe=False)
    else : 
        raise Http404()

    