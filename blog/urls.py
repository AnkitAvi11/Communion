from django.urls import path, re_path

from . import views

urlpatterns = [
    path('all/', views.allBlogs, name='allblogs'),
    path('addblog/', views.addBlog, name='addblog'),
    path('like/', views.likeBlog, name='likeblog'),

    #   slug field always at the bottom
    path('read/<slug:blog_id>/', views.viewBlog, name='read'),
    path('edit/<slug:blog_title>/', views.editBlog, name='editblog'),
    path('delete/<slug:blog_title>/', views.deleteBlog, name='deleteblog'),
]