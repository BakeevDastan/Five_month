from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Sum


# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @property
    def movies_count(self):
        return self.movies.all().count()

    def detail_link(self):
        return f'http://127.0.0.1:8000/api/v1/directors/{self.id}'


class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    duration = models.TimeField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies', null=True)

    def __str__(self):
        return self.title

    @property
    def reviews(self):
        review = Review.objects.filter(movie=self)
        return [{'text'} for i in review]

    @property
    def rating(self):
        summa = Review.objects.all().aggregate(Sum('stars'))["stars__sum"]
        count = Review.objects.all().count()
        try:
            return summa / count
        except:
            return 0

    def detail_link(self):
        return f'http://127.0.0.1:8000/api/v1/movies/{self.id}'


class Review(models.Model):
    text = models.TextField(null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews', null=True)
    stars = models.PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])

    def detail_link(self):
        return f'http://127.0.0.1:8000/api/v1/reviews/{self.id}'
