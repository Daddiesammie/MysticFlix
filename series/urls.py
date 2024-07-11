from django.urls import path
from . import views

urlpatterns = [
    path('', views.series_list, name='series_list'),
    path('<int:series_id>/', views.series_detail, name='series_detail'),
    path('<int:series_id>/season/<int:season_id>/', views.season_detail, name='season_detail'),
    path('<int:series_id>/season/<int:season_id>/episode/<int:episode_id>/', views.episode_detail, name='episode_detail'),
]
