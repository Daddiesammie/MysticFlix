# movie_media/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),  # Root URL now points to movie_list
    path('movies/', views.movie_list, name='movie_list'),
    path('drama/', views.drama_list, name='drama_list'),
    path('music_videos/', views.music_videos_list, name='music_videos_list'),
    path('animations/', views.animation_list, name='animation_list'),
    path('movies/<int:pk>/', views.movie_detail, name='movie_detail'),
    # path('search/', views.movie_search, name='movie_search'),
    # Add other URL patterns as needed
]
