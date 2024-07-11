from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    release_year = models.IntegerField()
    rating = models.FloatField()
    description = models.TextField()
    trailer_url = models.URLField(null=True, blank=True)
    download_link = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='movies/images/', null=True)
    released = models.BooleanField(default=True)
    drama = models.BooleanField(default=True)
    animation = models.BooleanField(default=True)
    music_video = models.BooleanField(default=True)
    featured = models.BooleanField(default=True)
    series = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='movies')
    def __str__(self):
        return self.title
    
