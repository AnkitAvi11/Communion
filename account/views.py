#   views related imports
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

#   user authentication related imports
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#   custom imports
from .decorators import isLoggedin
from .models import UserProfile

@isLoggedin
def userLogin(request) : 
    if request.method == 'POST' : 
        pass
    else : 
        return render(request, 'account/login.html')


@isLoggedin
def userSignup(request) : 
    if request.method == 'POST' : 
        username = request.POST.get('username')
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists() : 
            messages.error(request, 'User with that credentials already exist')
            return redirect('/account/signup/')
        else : 
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)

            userprofile = UserProfile(user=user)

            user.save()
            userprofile.save()

            messages.success(request, 'User registeration successful. Login to continue')
            return redirect('/account/login/')
        
    else : 
        return render(request, "account/signup.html")