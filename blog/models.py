from django.db import models 

from django.contrib.auth.models import User
from django.utils import timezone

class Blog(models.Model) : 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    #   slug = models.TextField()
    description = models.TextField(blank=False, null=False)
    body = models.TextField()
    cover_image = models.ImageField(upload_to = 'blogs/%Y/%m/', blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now())


    def __str__(self) : 
        return self.title