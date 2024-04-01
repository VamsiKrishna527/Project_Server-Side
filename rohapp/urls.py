from django.urls import path
from .views import ActorsList, MoviesList, home, CreateMovieView, ActorMovieDeleteView

urlpatterns = [
    path('',home,name='Home'),
    path('actors/', ActorsList.as_view(), name='actors-list'),
    path('movies/', MoviesList.as_view(), name='movies-list'),
    path('movies/create/',CreateMovieView.as_view(), name='create_movie_for_actor'),
    path('movies/delete/', ActorMovieDeleteView.as_view(), name="actor_movie_delete"),
]