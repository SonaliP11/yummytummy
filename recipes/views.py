from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Recipe
from .forms import CommentForm


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
    comments = recipe.comments.all().order_by("-created_on")
    comment_count = recipe.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.recipe = recipe
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )


    comment_form = CommentForm()


    return render(
        request, 
        template_name, 
        {
            "recipe": recipe,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,    
         },
        )

    
# Compare this snippet from recipes/views.

