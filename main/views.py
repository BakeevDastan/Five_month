from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, MovieWithReviewSerializer
from .models import Director, Movie, Review
from rest_framework import status


@api_view(['GET', 'POST'])
def director_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        director = Director.objects.create(
            name=request.data.get('name')
        )
        return Response(data=DirectorSerializer(director).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Post not found'})
    if request.method == "GET":
        serializer = DirectorSerializer(director)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        director = Director.objects.create(
            **request.data
        )
        return Response(data=DirectorSerializer(director).data,
                        status=status.HTTP_202_ACCEPTED)
    else:
        director.delete()
        return Response(data={'message': 'Director has been deleted'},
                        status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def movie_view(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        movie = Movie.objects.create(
            title=request.data.get('title'),
            description=request.data.get('description'),
            duration=request.data.get('duration'),
        )
        return Response(data=MovieSerializer(movie).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': ' Post not found'})
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        movie = Movie.objects.create(
            title=request.data.get('title'),
            description=request.data.get('description'),
            duration=request.data.get('duration'),
        )
        return Response(data=MovieSerializer(movie).data,
                        status=status.HTTP_201_CREATED)
    else:
        movie.delete()
        return Response(data={'message': 'Director has been deleted'},
                        status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def review_view(request):
    if request.method == "GET":
        review = Review.objects.all()
        serializer = ReviewSerializer(review, many=True)
        return Response(data=serializer.data)
    elif request.method == "POST":
        review = Review.objects.create(
            text=request.data.get("text"),
            movie_id=request.data.get("movie_id"),
            stars=request.data.get("stars"),
        )
        return Response(data=ReviewSerializer(review).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': ' Post not found'})
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        review = Review.objects.create(
            text=request.data.get("text"),
            movie_id=request.data.get("movie_id"),
            stars=request.data.get("stars"),
        )
        return Response(data=ReviewSerializer(review).data,
                        status=status.HTTP_201_CREATED)
    else:
        review.delete()
        return Response(data={'message': 'Director has been deleted'},
                        status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def movie_review_view(request):
    movie_review = Movie.objects.all()
    data = MovieWithReviewSerializer(movie_review, many=True).data
    return Response(data=data)
