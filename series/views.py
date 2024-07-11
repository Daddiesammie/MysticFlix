from django.shortcuts import render, get_object_or_404
from .models import Series, Season, Episode

def series_list(request):
    series = Series.objects.all()
    return render(request, 'series/series_list.html', {'series': series})

def series_detail(request, series_id):
    series = get_object_or_404(Series, id=series_id)
    seasons = series.seasons.all()
    return render(request, 'series/series_detail.html', {'series': series, 'seasons': seasons})

def season_detail(request, series_id, season_id):
    season = get_object_or_404(Season, id=season_id, series_id=series_id)
    episodes = season.episodes.all()
    return render(request, 'series/season_detail.html', {'season': season, 'episodes': episodes})

def episode_detail(request, series_id, season_id, episode_id):
    episode = get_object_or_404(Episode, id=episode_id, season_id=season_id)
    return render(request, 'series/episode_detail.html', {'episode': episode})
