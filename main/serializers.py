from rest_framework import serializers
from .models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name movies_count detail_link'.split()


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'title description duration director detail_link'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text movie stars detail_link'.split()


class MovieWithReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    director = DirectorSerializer()

    class Meta:
        model = Movie
        fields = ' id title description duration director reviews rating'.split()


class DirectorCountSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = 'movies_count'.split()

    def get_movie_count(self, movie):
        return movie.all().count()
