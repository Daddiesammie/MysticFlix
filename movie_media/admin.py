# movie_media/admin.py

from django.contrib import admin
from .models import Movie, Category



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'genre', 'release_year', 'rating')
    list_filter = ('genre', 'release_year', 'rating')
    search_fields = ('title', 'description')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Movie, MovieAdmin)
