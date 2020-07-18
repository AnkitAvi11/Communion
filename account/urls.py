from django.urls import path, re_path

from . import views

urlpatterns = [
    path('login/', views.userLogin, name='login'),
    path('signup/', views.userSignup, name='signup'),
    path('logoutuser/', views.logoutuser, name='logoutuser')
]