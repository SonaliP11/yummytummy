from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Recipe


# Create your views here.
class RecipeList(generic.ListView):
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'recipes/index.html'
    paginate_by = 9


def recipe_detail(request, slug):
    """
    Display an individual :model:`recipes.Recipe`.

    **Context**

    ``recipe``
        An instance of :model:`recipes.Recipe`.

    **Template:**

    :template:`recipes/recipe_detail.html`
    """
    template_name = 'recipes/recipe_detail.html'
    
    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)

    return render(
        request, 
        template_name, 
        {"recipe": recipe},
        )

    
# Compare this snippet from recipes/views.

