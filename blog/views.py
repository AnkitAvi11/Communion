from django.shortcuts import render, redirect
from .models import Blog

def allBlogs(request) : 
    blogs = Blog.objects.all()
    context = {
        "blogs" : blogs
    }
    
    return render(request, 'pages/blogs.html', context)