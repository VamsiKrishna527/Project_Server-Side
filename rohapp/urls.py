from django.urls import path
from .views import ActorsList, MoviesList, home, create_movie_for_actor

urlpatterns = [
    path('',home,name='Home'),
    path('actors/', ActorsList.as_view(), name='actors-list'),
    path('movies/', MoviesList.as_view(), name='movies-list'),
    path('post/',create_movie_for_actor, name='create_movie_for_actor'),
]