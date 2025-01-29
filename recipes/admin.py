from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe) 
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'meal_type', 'author','status')
    search_fields = ['title']
    list_filter = ('status', 'meal_type',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description', 'ingredients', 'steps',)

# Register your models here.
admin.site.register(Comment)