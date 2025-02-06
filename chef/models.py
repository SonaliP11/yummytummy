from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Chef(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_image = CloudinaryField('image', null=True, blank=True)

    
    def __str__(self):
        return self.name
    