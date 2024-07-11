from django.apps import AppConfig

class MovieMediaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movie_media'

    def ready(self):
        import movie_media.signals # type: ignore