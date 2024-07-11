from django.shortcuts import render
from movie_media.models import Movie
from .models import About

def about(request):
    movies = Movie.objects.all()
    about_content = About.objects.first()  # Assuming there will be only one About entry
    return render(request, 'about/about.html', {'about_content': about_content, 'movies': movies,})
