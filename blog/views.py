from django.shortcuts import render, redirect
from .models import Blog
from django.contrib.auth.decorators import login_required
from django.forms import forms
from django_summernote.fields import SummernoteTextFormField
from django.http import Http404, HttpResponse, JsonResponse
from django.utils.text import slugify
from django.contrib import messages
from django.core.paginator import Paginator
import string
import random

from account.models import Notifications
from datetime import datetime

def random_string_generator(size = 10, chars = string.ascii_lowercase + string.digits): 
    return ''.join(random.choice(chars) for _ in range(size))

def allBlogs(request) : 
    if request.user.is_authenticated : 
        blogs = Blog.objects.all().exclude(user=request.user).order_by('-created_on')
    else : 
        blogs = Blog.objects.all().order_by('-created_on')

    cover = blogs.exclude(cover_image__exact="").exclude(cover_image__isnull=True)

    paginator = Paginator(blogs, 10)
    page = request.GET.get('page')
    paged_blogs = paginator.get_page(page)

    import random

    context = {
        "blogs" : paged_blogs,
        "cover" : random.choice(cover)
    }
    
    return render(request, 'pages/blogs.html', context)


class AddBlogForm(forms.Form) : 
    body = SummernoteTextFormField()

@login_required(login_url='/account/login')
def addBlog(request) : 
    if request.method == 'POST' : 
        title = request.POST.get('title')
        slug = slugify(title)

        while Blog.objects.filter(slug_title=slug).exists() : 
            randstr = random_string_generator(size=10)
            slug = "{}-{}".format(slug, randstr)

        description = request.POST.get('description')
        body = request.POST.get('body')
        cover_image = request.FILES.get('cover')
        from datetime import datetime
        created_on = datetime.now()
        try : 
            blog = Blog(
                user = request.user,
                title = title,
                slug_title = slug,
                description = description,
                body = body,
                cover_image = cover_image,
                created_on = created_on,
                published = True
            )
            blog.save()
            messages.success(request, 'Blog posted successfully')
            return redirect('/blog/addblog')
        except Exception as e : 
            messages.error(request, e)
            return render(request, 'pages/addblog.html', {"form" : AddBlogForm})
    else : 
        return render(request, 'pages/addblog.html', {"form" : AddBlogForm})

def viewBlog(request, blog_id) : 
    try : 
        blog = Blog.objects.get(slug_title=blog_id)
        
        if blog is not None : 
            return render(request, 'pages/viewblog.html', {"blog" : blog})
        else : 
            raise Http404()
    except Exception as e : 
        raise Http404()


@login_required(login_url='/account/login/')
def likeBlog(request) : 
    if request.method == 'POST' : 
        user = request.user
        blog_id = request.POST.get('blog_id')
        blog = Blog.objects.get(id=blog_id)
        if user in blog.likes.all() : 
            blog.likes.remove(user)
            return JsonResponse({
                'message' : 'LIKE',
                'action' : 'DISLIKE',
                'likes' : blog.likes.count()
            })
        else : 
            blog.likes.add(user)
            if user!=blog.user : 
                Notifications.objects.create(user=blog.user, title='{} liked your blog'.format(user), time_created = datetime.now(), link="/blog/read/{}".format(blog.slug_title))
            return JsonResponse({
                'message' : 'DISLIKE',
                'action' : 'LIKE',
                'likes' : blog.likes.count()
            })
    else :
        messages.error(request, 'You need to be loggedin')
        return redirect('/account/login/')


@login_required(login_url='/account/login/')
def editBlog(request, blog_title) : 
    if request.method == 'POST' : 
        title = request.POST.get('title')
        slug = slugify(title)

        while Blog.objects.filter(slug_title=slug).exists() : 
            randstr = random_string_generator(size=10)
            slug = "{}-{}".format(slug, randstr)

        description = request.POST.get('description')
        body = request.POST.get('body')
        cover_image = request.FILES.get('cover')
        from datetime import datetime
        created_on = datetime.now()

        Blog.objects.filter(slug_title=blog_title).update(title=title, slug_title=slug, description=description, created_on=created_on, body=body)

        blog = Blog.objects.get(slug_title=slug)
        blog.cover_image = cover_image
        blog.save()

        messages.success(request, 'Blog updated successfully')
        return redirect('/blog/edit/{}/'.format(slug))

    else : 
        blog = Blog.objects.get(slug_title__exact=blog_title)
        form = AddBlogForm(initial={'body' : blog.body})
        return render(
            request,
            'pages/editblog.html',
            {"blog" : blog, "form" : form}
        )

#   method view to delete a particular post of the user
@login_required(login_url = '/account/login/')
def deleteBlog(request, blog_title) : 
    blog = Blog.objects.get(user=request.user, slug_title__exact = blog_title)
    blog.delete()
    return redirect('/@{}/'.format(request.user.username))