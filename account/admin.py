from django.contrib import admin

# Register your models here.
from .models import UserProfile, Follower, Notifications

class UserprofileAdmin(admin.ModelAdmin) : 
    list_display = ('id', 'user', 'profile_image', 'summary')
    list_display_links = ('id', 'user')

class NotificationsAdmin(admin.ModelAdmin) : 
    list_display = ('id', 'title', 'description')
    list_display_links = ('id', 'title')

admin.site.register(UserProfile, UserprofileAdmin)
admin.site.register(Follower)
admin.site.register(Notifications, NotificationsAdmin)
