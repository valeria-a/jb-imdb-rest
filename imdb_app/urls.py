"""imdb_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from imdb_app import views

# http://127.0.0.1:8000/api/imdb/movies
# movies

# http://127.0.0.1:8000/api/imdb/movies/3
# http://127.0.0.1:8000/api/imdb/movies/327

urlpatterns = [
    path('movies', views.get_movies),
    path('movies/<int:movie_id>', views.get_movie),
    path('movies/<int:movie_id>/actors', views.movie_actors),
    path('movies/<int:movie_id>/actors/<int:actor_id>', views.movie_actor),
    path('movies/<int:movie_id>/ratings', views.movie_ratings),
    path('movies/<int:movie_id>/ratings/<int:rating_id>', views.movie_rating),

    path('actors', views.actors),
    path('actors/<int:actor_id>', views.actor_details),

    path('ratings', views.get_ratings),
    path('movies/<int:movie_id>/ratings', views.get_movie_ratings),
    path('movies/<int:movie_id>/ratings/avg', views.get_avg_movie_rating),
]
