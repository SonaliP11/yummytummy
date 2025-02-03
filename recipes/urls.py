from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('<str:meal_type>/', views.RecipeList.as_view(), name='filtered_recipes'),
    path('<slug:slug>/', views.recipe_detail, name='recipe_detail'),
]