from django.urls import path, re_path

from . import views

urlpatterns = [
    #   named paths here (fixed name)
    path('', views.homePage, name='home'),

    #   paths starting with regular expressions here
    re_path(r'^@(?P<username>[a-zA-Z0-9\-\_\.]+)/$', views.viewUser, name='viewuser'),
]