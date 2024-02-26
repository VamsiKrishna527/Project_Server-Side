from django.urls import path
from .views import ActorsList, MoviesList, home

urlpatterns = [
    path('',home,name='Home'),
    path('actors/', ActorsList.as_view(), name='actors-list'),
    path('movies/', MoviesList.as_view(), name='movies-list'),
]