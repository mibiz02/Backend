from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_title = models.CharField(max_length=50)
    movie_poster_path = models.TextField()
    tmdb_id = models.IntegerField()
    movie_description = models.TextField()