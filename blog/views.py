from django.shortcuts import render, redirect
from .models import Blog
from django.contrib.auth.decorators import login_required
from django.forms import forms
from django_summernote.fields import SummernoteTextFormField
from django.http import Http404, HttpResponse, JsonResponse
from django.utils.text import slugify
from django.contrib import messages

def allBlogs(request) : 
    blogs = Blog.objects.all().exclude(user=request.user).order_by('-created_on')
    context = {
        "blogs" : blogs
    }
    
    return render(request, 'pages/blogs.html', context)


class AddBlogForm(forms.Form) : 
    body = SummernoteTextFormField()

@login_required(login_url='/account/login')
def addBlog(request) : 
    if request.method == 'POST' : 
        title = request.POST.get('title')
        slug = slugify(title)
        description = request.POST.get('description')
        body = request.POST.get('body')
        cover_image = request.FILES.get('cover')
        from datetime import datetime
        created_on = datetime.now()
        try : 
            Blog.objects.create(
                user = request.user,
                title = title,
                slug_title = slug,
                description = description,
                body = body,
                cover_image = cover_image,
                created_on = created_on,
                published = True
            )
            messages.success(request, 'Blog posted successfully')
            return redirect('/blog/addblog')
        except Exception as e : 
            messages.error(request, e.message)
            return render(request, 'pages/addblog.html', {})
    else : 
        return render(request, 'pages/addblog.html', {"form" : AddBlogForm})

def viewBlog(request, slug) : 
    try : 
        blog = Blog.objects.get(slug_title=slug)
        print(blog)
        if blog is not None : 
            return render(request, 'pages/viewblog.html', {"blog" : blog})
        else : 
            raise Http404()
    except Exception as e : 
        raise Http404()