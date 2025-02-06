from django.contrib import admin
from .models import ChefProfile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(ChefProfile)
class ChefProfileAdmin(SummernoteModelAdmin):

    summernote_fields = ('bio',)

