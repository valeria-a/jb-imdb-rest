from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from imdb_app.models import *
from imdb_app.serializers import MovieSerializer, ActorSerializer


# Create your views here.

# @api_view(['GET'])
# def get_movies(request):
#     all_movies = Movie.objects.all()
#     data = []
#     for movie in all_movies:
#         data.append({
#             'id': movie.pk,
#             'name': movie.name,
#             'release_year': movie.release_year,
#             'description': movie.description,
#             'duration_in_min': movie.duration_in_min,
#             'actors': []
#         })
#     return Response(data=data)


@api_view(['GET'])
def get_movies(request):
    all_movies = Movie.objects.all()
    serializer = MovieSerializer(instance=all_movies, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def get_actors(request):
    all_actors = Actor.objects.all()
    serializer = ActorSerializer(instance=all_actors, many=True)
    return Response(data=serializer.data)