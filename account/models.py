from django.db import models

from django.contrib.auth.models import User
from django.utils.timezone import timezone, timedelta
from datetime import datetime

class UserProfile(models.Model) : 

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to = 'images/%Y/%m/', default='default.png', blank=True)
    summary = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    learning = models.TextField(blank=True)
    project_description = models.TextField(blank=True)
    available_for = models.TextField(blank=True)
    show_email = models.BooleanField(default=False)

    def __str__(self) : 
        return self.user.username

    #   overriding the save function to delete the old profile picture if a user uploads a new profile picture
    def save(self, *args, **kwargs) : 
        try : 
            current = UserProfile.objects.get(id=self.id)
            if current.profile_image != self.profile_image and current.profile_image!='default.png' : 
                current.profile_image.delete()
        except : 
            pass
        super().save(*args, **kwargs)


    #   overriding the delete method to delete redundant images
    def delete(self, *args, **kwargs) : 
        self.profile_image.delete()
        super().delete(*args, **kwargs)


#   Model for creating relation between users if they follow
class Follower(models.Model) : 

    user_from = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='from_set')
    user_to = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='to_set')
    relation_date = models.DateTimeField(default=datetime.now())

    def __str__(self) : 
        return "{} follows {}".format(self.user_from, self.user_to)

    def isFollowing(self, u_from, to) : 
        if Follower.objects.filter(user_from=u_from, user_to = to).exists() : 
            return True
        else : 
            return False
        
