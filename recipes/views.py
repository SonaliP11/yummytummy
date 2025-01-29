from django.shortcuts import render
from django.views import generic
from .models import Recipe


# Create your views here.
class RecipeList(generic.ListView):
    model = Recipe

class RecipeDetail(generic.DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    
# Compare this snippet from recipes/views.

