from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

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
def get_movies(request: Request):
    all_movies = Movie.objects.all()
    print("initial query:", all_movies.query)

    if 'name' in request.query_params:
        all_movies = all_movies.filter(name__iexact=request.query_params['name'])
        print("after adding name filter", all_movies.query)
    if 'duration_from' in request.query_params:
        all_movies = all_movies.filter(duration_in_min__gte=request.query_params['duration_from'])
        print("after adding duration_from filter", all_movies.query)
    if 'duration_to' in request.query_params:
        all_movies = all_movies.filter(duration_in_min__lte=request.query_params['duration_to'])
        print("after adding duration_to filter", all_movies.query)
    if 'description' in request.query_params:
        all_movies = all_movies.filter(description__icontains=request.query_params['description'])
        print("after adding description filter", all_movies.query)

    serializer = MovieSerializer(instance=all_movies, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def get_actors(request):
    all_actors = Actor.objects.all()
    serializer = ActorSerializer(instance=all_actors, many=True)
    return Response(data=serializer.data)
