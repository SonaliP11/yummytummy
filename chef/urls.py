from . import views
from django.urls import path

urlpatterns = [
    path('', views.chef_detail, name='chef'),
]