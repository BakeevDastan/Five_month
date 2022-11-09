from rest_framework import serializers
from .models import Director, Movie, Review
from rest_framework.exceptions import ValidationError


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


class MovieValidateUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=3, max_length=50)
    description = serializers.CharField()
    duration = serializers.IntegerField(required=False)
    director_id = serializers.IntegerField()

    def validate_title(self, title):
        if Movie.objects.filter(title=title):
            raise ValidationError("Select unique name for your movie")
        return title


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    movie_id = serializers.IntegerField()
    stars = serializers.IntegerField(required=False, max_value=5)

    def validate_movie_id(self, movie_id):
        try:
            Review.objects.get(movie_id=movie_id)
        except:
            raise ValidationError("Choose correct id movie")
        return movie_id


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)

    def validate_name(self, name):
        if Director.objects.filter(name=name):
            raise ValidationError("This name is already exists")
        return name
