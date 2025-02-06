from django.shortcuts import render
from .models import Chef


def chef_display(request):
    """
    Renders the Chef page
    """
    chef = Chef.objects.all()

    return render(
        request,
        "chef/chef.html",
        {"chef": chef},
    )