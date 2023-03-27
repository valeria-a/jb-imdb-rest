from rest_framework import serializers

from imdb_app.models import Movie


# class MovieSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     release_year = serializers.IntegerField()
#     description = serializers.CharField()


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        # fields = ['id', 'name', 'release_year', 'duration_in_min', 'pic_url']
        # exclude = ['pic_url']
        # depth = 1
