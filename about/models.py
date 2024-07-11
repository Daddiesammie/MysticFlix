from django.db import models

class About(models.Model):
    heading = models.CharField(max_length=200)
    sub_heading = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='about_images/', blank=True, null=True)

    def __str__(self):
        return self.heading
