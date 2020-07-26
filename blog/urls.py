from django.urls import path, re_path

from . import views

urlpatterns = [
    path('all/', views.allBlogs, name='allblogs'),
    path('addblog/', views.addBlog, name='addblog'),
    path('read/<slug:slug>/', views.viewBlog, name='read')
]