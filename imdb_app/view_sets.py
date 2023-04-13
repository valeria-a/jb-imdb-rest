from rest_framework.viewsets import ModelViewSet

from imdb_app.models import Movie
from imdb_app.serializers import MovieSerializer


class MovieViewSet(ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()