from django.shortcuts import render
from django.http import HttpResponse

def my_recipes(request):
    return HttpResponse("Hello, Recipe!")

# Create your views here.
