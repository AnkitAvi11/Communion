from django.urls import path, re_path

from . import views

urlpatterns = [
    path('login/', views.userLogin, name='login'),
    path('signup/', views.userSignup, name='signup'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    path('setting/', views.userSetting, name='usersetting'),
    path('followuser/', views.followUser, name='follow'),
    path('emailsetting/', views.emailSetting, name='emailsetting'),
    path('changepassword/', views.changePassword, name='changepassword'),
]