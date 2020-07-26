from django.db import models 

from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class Blog(models.Model) : 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    slug_title = models.TextField(null=True, blank=True)
    description = models.TextField(blank=False, null=False)
    body = models.TextField()
    cover_image = models.ImageField(upload_to = 'blogs/%Y/%m/', blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now())
    published = models.BooleanField(default=True)
    likes = models.ManyToManyField(User, related_name='user_likes', null=True, blank=True)

    def __str__(self) : 
        return self.title

    def is_recent(self) : 
        return True if self.created_on >= (timezone.now()-timedelta(days=2)) else False