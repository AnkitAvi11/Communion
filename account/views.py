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
from .models import UserProfile, Follower, Notifications
from datetime import datetime

def getPost(request, key) : 
    return request.POST.get(key)

import re
def isValidEmail(email) : 
    regex = re.compile('^([a-zA-Z0-9\.\-\_])+\@([a-zA-Z0-9\.\-\_])+\.([a-zA-Z0-9]{2,4})$')
    return re.match(regex, email)

def isvalidUsername(username) :
    regex = re.compile('^([a-zA-Z0-9\_@])+$')
    return re.match(regex, username)


#   login request handler
@isLoggedin
def userLogin(request) : 
    if request.method == 'POST' : 
        username = request.POST.get('username')
        if (isValidEmail(username)) : 
            username = User.objects.get(email=username).username

        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None : 
            login(request, user)
            return redirect('/')
        else : 
            messages.error(request, 'Invalid username/email or password')
            return redirect('/account/login/')
        
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

        if not isValidEmail(email) : 
            messages.error(request, "Enter a valid email address")
            return redirect("/account/signup")

        if not isvalidUsername(username) : 
            messages.error(request, "Enter a valid username")
            return redirect("/account/signup")

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


def logoutuser(request) : 
    if request.method == 'POST' : 
        logout(request)
        return redirect('/')
    else : 
        return redirect('/')

@login_required(login_url='/account/login/')
def userSetting(request) : 
    if request.method == 'POST' : 
        first_name = getPost(request, 'fname')
        last_name = getPost(request, 'lname')
        User.objects.filter(username=request.user).update(first_name=first_name, last_name=last_name)

        profile_image = request.FILES.get('profile_image', request.user.userprofile.profile_image)

        request.user.userprofile.profile_image = profile_image;
        request.user.userprofile.save()

        summary = getPost(request, 'summary')
        skills = getPost(request, 'skills')
        learning = getPost(request, 'learning')
        project_description = getPost(request, 'project')
        available_for = getPost(request, 'available')

        UserProfile.objects.filter(user=request.user).update(
            summary = summary,
            skills = skills,
            learning = learning,
            project_description = project_description,
            available_for = available_for
        )

        messages.success(request, 'User profile saved successfully')
        return redirect("/account/setting/")

    else : 
        return render(request, 'account/settings.html')

@login_required(login_url='/account/login/')
def emailSetting(request) : 
    if request.method == 'POST' : 
        user = request.user
        show = request.POST.get('show_email')
        show_email = True if show == 'on' else False
        UserProfile.objects.filter(user=user).update(show_email=show_email)
        messages.success(request, 'Email Updated successfully')
        return redirect('/account/setting')
    else : 
        return redirect('/')

@login_required(login_url='/account/login/')
def followUser(request) :
    if request.method == 'POST' : 
        user_from = request.user;user_to = request.POST.get("follow_to")

        user_to = User.objects.get(id=user_to)
        
        if Follower.objects.filter(user_from=user_from, user_to=user_to).exists() : 
            follow = Follower.objects.get(user_from=user_from,user_to=user_to)
            follow.delete()
            return JsonResponse({
                "message" : "Follow",
                "Action Performed" : "Unfollow" 
            })
        else : 
            Follower.objects.create(user_from = user_from, user_to = user_to)
            Notifications.objects.create(user=user_to, title="{} started following you".format(user_from), time_created=datetime.now(), link="/@{}".format(user_from))
            return JsonResponse({
                "message" : "Unfollow",
                "Action Performed" : "Follow" 
            })

    else : 
        return redirect("/")


@login_required(login_url='/account/login/')
def changePassword(request) : 
    if request.method == 'POST' : 
        cpassword = getPost(request, 'cpassword')
        password1 = getPost(request, 'password1')
        password2 = getPost(request, 'password2')

        user = authenticate(username=request.user, password=cpassword)

        if user is not None : 
            if password1 == password2 : 
                user.set_password(password1)
                user.save()
                messages.success(request, 'Password changed successfully. Login again to continue.')
                return redirect('/account/setting/')
            else : 
                messages.error(request, 'Password did not match')
                return redirect('/account/setting/')
        else : 
            messages.error(request, 'Incorrect password')
            return redirect('/account/setting/')

    else :
        return redirect("/")