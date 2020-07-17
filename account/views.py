#   views related imports
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

#   user authentication related imports
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

#   custom imports
from .decorators import isLoggedin

@isLoggedin
def userLogin(request) : 
    if request.method == 'POST' : 
        pass
    else : 
        return HttpResponse('Login page')
