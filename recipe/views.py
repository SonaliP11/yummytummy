from django.shortcuts import render
from django.http import HttpResponse

def my_recipe(request):
    return HttpResponse("Hello, Recipe!")

# Create your views here.
