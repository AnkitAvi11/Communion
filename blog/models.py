from django.db import models 

from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class Blog(models.Model) : 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    #   slug = models.TextField()
    description = models.TextField(blank=False, null=False)
    body = models.TextField()
    cover_image = models.ImageField(upload_to = 'blogs/%Y/%m/', blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now())
    published = models.BooleanField(default=True)

    def __str__(self) : 
        return self.title

    def is_recent(self) : 
        return True if self.created_on >= (timezone.now()-timedelta(days=2)) else False