from django.db import models 

from django.contrib.auth.models import User

class Blog(models.Model) : 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    