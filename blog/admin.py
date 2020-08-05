from django.contrib import admin

# Register your models here.
from .models import Blog
from django_summernote.admin import SummernoteModelAdmin

class BlogAdmin(SummernoteModelAdmin) : 
    summernote_fields = ('body')
    list_display = ('id', 'title', 'user', 'description', 'created_on')
    list_display_links = ('id', 'title')

admin.site.register(Blog, BlogAdmin)