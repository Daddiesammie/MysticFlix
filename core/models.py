from django.db import models

class SiteConfiguration(models.Model):
    site_name = models.CharField(max_length=255)
    site_logo = models.ImageField(upload_to='site/logo/', null=True, blank=True)
    site_favicon = models.ImageField(upload_to='site/favicon/', null=True, blank=True)
    disclaimer = models.TextField(null=True, blank=True)
    facebook_link = models.URLField(null=True, blank=True)
    twitter_link = models.URLField(null=True, blank=True)
    instagram_link = models.URLField(null=True, blank=True)
    linkedin_link = models.URLField(null=True, blank=True)
    youtube_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.site_name
