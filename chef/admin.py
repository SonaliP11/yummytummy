from django.contrib import admin
from .models import Chef
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Chef)
class ChefAdmin(SummernoteModelAdmin):

    summernote_fields = ('bio',)