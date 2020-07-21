from django.db import models

from django.contrib.auth.models import User

class UserProfile(models.Model) : 

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to = 'images/%Y/%m/', default='default.png', blank=True)
    summary = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    learning = models.TextField(blank=True)
    project_description = models.TextField(blank=True)
    available_for = models.TextField(blank=True)

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


#   model for followers and following
class Follower(models.Model) : 
    user = models.ManyToManyField(User)


    def __str__(self) : 
        return self.user.username