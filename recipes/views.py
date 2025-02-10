from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Count
from django.contrib.auth.models import User
from .models import Recipe, Comment
from .forms import CommentForm


# Create your views here.

def chef(request):
    """
    Display the chef page.

    **Context**

    ``top_chefs``
        A list of dictionaries containing the top chefs
        and their recipe counts.

    **Template:**

    :template:`recipes/chef.html`
    """
    recipes = Recipe.objects.values(
              'author__username', 'author__id').annotate(recipe_count=Count(
              'author')).order_by('-recipe_count')[:2]
    top_chefs = []

    for recipe in recipes:
        user = get_object_or_404(User, id=recipe['author__id'])
        top_chefs.append({
            'username': user.username,
            'recipe_count': recipe['recipe_count'],
            'recipes': Recipe.objects.filter(author=user)
        })

    template_name = 'recipes/chef.html'
    return render(request, template_name, {"top_chefs": top_chefs})


class RecipeList(generic.ListView):
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'recipes/index.html'
    paginate_by = 12


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
            "rating_choices": Comment.rating.field.choices,
         },
        )


def comment_edit(request, slug, comment_id):

    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))
