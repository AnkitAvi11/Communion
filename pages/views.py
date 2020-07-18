from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

def homePage(request) : 
    if request.user.is_authenticated : 
        return render(request, 'pages/home.html')
    else : 
        return render(request, 'pages/index.html')