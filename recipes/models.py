from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Choice fields
MEAL_TYPES = (
    ('breakfast', 'Breakfast'),
    ('lunch', 'Lunch'),
    ('dinner', 'Dinner'),
)

# Create your models here.
class Recipe(models.Model):
    """
    Model representing a recipe
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipe_owner') 
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    ingredients = models.TextField()
    steps = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    meal_type = models.CharField(max_length=50, choices=MEAL_TYPES, default='breakfast')
    class Meta:
        ordering = ["-posted_date"]  
    
    def __str__(self):
        return self.title