from django.contrib import admin

# Register your models here.
from .models import Blog

class BlogAdmin(admin.ModelAdmin) : 
    list_display = ('id', 'title', 'created_on', 'description', 'body')
    list_display_links = ('id', 'title')


admin.site.register(Blog, BlogAdmin)