from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=255)
    imdb_score = models.FloatField(blank=True, null=True)
    popularity = models.FloatField(blank=True, null=True)
    director = models.ForeignKey(Director, on_delete=models.DO_NOTHING)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name