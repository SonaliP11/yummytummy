from django.shortcuts import render
from .models import ChefProfile


def chef_detail(request):
    """
    Renders the ChefProfile page
    """
    chef = ChefProfile.objects.all()

    return render(
        request,
        "chef/chef.html",
        {"chef": chef},
    )