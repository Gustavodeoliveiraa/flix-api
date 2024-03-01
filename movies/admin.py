from django.contrib import admin
from .models import Movies


@admin.register(Movies)
class AdminMovies(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'genre', 'release_date', 'resume'
    )
