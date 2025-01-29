from django.shortcuts import render
from django.views import generic
from .models import Recipe


# Create your views here.
class RecipeList(generic.ListView):
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'recipes/recipe_list.html'

class RecipeDetail(generic.DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    
# Compare this snippet from recipes/views.

