from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))

# Choice fields
MEAL_TYPES = (
    ('breakfast', 'Breakfast'),
    ('lunch', 'Lunch'),
    ('dinner', 'Dinner'),
)

STAR_RATINGS = (
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐'),
    )

# Create your models here.
class Recipe(models.Model):
    """
    Model representing a recipe
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipe_owner') 
    title = models.CharField(max_length=200, unique=True, blank=False, null=False)
    description = models.TextField(null=False, blank=False)
    ingredients = models.TextField()
    steps = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    featured_image = CloudinaryField('image', default='placeholder')    
    status = models.IntegerField(choices=STATUS, default=0)
    meal_type = models.CharField(max_length=50, choices=MEAL_TYPES, default='breakfast')
    class Meta:
        ordering = ["-created_on"]  
    
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    """
    Model representing a comment
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    rating = models.IntegerField(choices=STAR_RATINGS, default=1)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-created_on"]  
    
    def __str__(self):
        return f"{self.body} by {self.author}"
