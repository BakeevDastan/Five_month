from unittest.util import _MAX_LENGTH
from django.db import models


# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def detail_link(self):
        return f'http://127.0.0.1:8000/api/v1/directors/{self.id}'


class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    duration = models.TimeField()
    director = models.ForeignKey(Director, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def detail_link(self):
        return f'http://127.0.0.1:8000/api/v1/movies/{self.id}'


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def detail_link(self):
        return f'http://127.0.0.1:8000/api/v1/reviews/{self.id}'