from django.shortcuts import render, get_object_or_404
from .models import Movie, Category


def drama_list(request):
    dramas = Movie.objects.filter(genre__icontains='drama')
    return render(request,'movie_media/drama_list.html', {'dramas': dramas})

def music_videos_list(request):
    music_videos = Movie.objects.filter(music_video=True)
    print("Music Videos: ", music_videos)  # Debug statement
    return render(request, 'movie_media/music_videos_list.html', {'music_videos': music_videos})

def animation_list(request):
    animations = Movie.objects.filter(genre__icontains='animation')
    return render(request, 'movie_media/animation_list.html', {'animations': animations})



def movie_list(request):
    query = request.GET.get('q', '')
    category_name = request.GET.get('category', '')
    genre = request.GET.get('genre', '')
    released = request.GET.get('released', '')
    
    movies = Movie.objects.all()

    if query:
        movies = movies.filter(title__icontains=query)
    
    if category_name and category_name != 'All Categories':
        movies = movies.filter(category__name=category_name)
    
    if genre:
        movies = movies.filter(genre__icontains=genre)
    
    if released:
        if released == 'True':
            movies = movies.filter(released=True)
        elif released == 'False':
            movies = movies.filter(released=False)
    
    categories = Category.objects.all()
    
    context = {
        'movies': movies,
        'categories': categories,
        'query': query,
        'category': category_name,
        'genre': genre,
        'released': released,
    }
    
    return render(request, 'movie_media/movie_list.html', context)


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    context = {'movie': movie}
    return render(request, 'movie_media/movie_detail.html', context)
