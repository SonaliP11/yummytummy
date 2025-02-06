from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class ChefProfile(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    bio = models.TextField()
    chef_image = CloudinaryField('chef_image', default='placeholder')
    interests = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    