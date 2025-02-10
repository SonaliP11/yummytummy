from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

"""
About model - to store information about the site owner
"""


class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    profile_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.title


class CollaborateRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    recipeName = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    recipe_image = CloudinaryField('collaboration_image',
                                   default='placeholder')
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"
