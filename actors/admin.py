from django.contrib import admin
from .models import Actors


@admin.register(Actors)
class AdminActors(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'birthday', 'nationality'
    )
