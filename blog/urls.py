from django.urls import path, re_path

from . import views

urlpatterns = [
    path('all/', views.allBlogs, name='allblogs'),
]