from . import views
from django.urls import path

urlpatterns = [
    path('', views.chef_display, name='chef'),
]