import django_filters
from django_filters import FilterSet
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from imdb_app.models import Movie
from imdb_app.serializers import MovieSerializer, DetailedMovieSerializer, CreateMovieSerializer, CastSerializer

class MoviePageClass(PageNumberPagination):
    page_size = 5
    # page_query_param = 'bbb'


class MovieFilterSet(FilterSet):

    name = django_filters.CharFilter(field_name='name', lookup_expr='iexact')
    duration_from = django_filters.NumberFilter('duration_in_min', lookup_expr='gte')
    duration_to = django_filters.NumberFilter('duration_in_min', lookup_expr='lte')
    description = django_filters.CharFilter(field_name='description', lookup_expr='icontains')

    class Meta:
        model = Movie
        fields = ['release_year']


class MoviePermission(BasePermission):

    def has_permission(self, request, view):
        print("inside has_permission")
        return request.user.is_staff or view.action \
            in ('list', 'retrieve')

    def has_object_permission(self, request, view, obj):
        print("inside has_object_permission", obj)
        return view.action == 'retrieve' or \
            obj.created_by == request.user
        # obj.created_by_id == request.user.id
class MovieViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   GenericViewSet):

    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    pagination_class = MoviePageClass
    filterset_class = MovieFilterSet
    # permission_classes = [IsAuthenticated]
    permission_classes = [MoviePermission]

    # movies/actors
    # movies/<movie_id>/actors
    # @action(methods=['GET'], detail=True, url_path='actors')
    # def actors(self):
    #     movie = self.get_object()
    #     all_casts = movie.movieactor_set.all()
    #     serializer = CastSerializer(instance=all_casts, many=True)
    #     return Response(data=serializer.data)

    # def get_permissions(self):
    #     if self.action in ('create', 'update', 'destroy'):
    #         return [IsAdminUser()]
    #     else:
    #         return []

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return DetailedMovieSerializer
        elif self.action == 'create':
            return CreateMovieSerializer
        else:
            return super().get_serializer_class()


    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



# class MovieActorSet(ModelViewSet):
#     pass