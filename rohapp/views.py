from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from .models import Actors, Movies
from .serializers import ActorSerializer, MovieSerializer
from rest_framework.decorators import api_view

def home(request):
    return HttpResponse("Welcome to the API!")


class ActorsList(generics.ListCreateAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorSerializer

class MoviesList(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

@api_view(['POST'])
def create_movie_for_actor(request):
    actor_id = request.data.get('actor_id')
    actor_instance = Actors.objects.get(pk=actor_id)

    if not actor_instance:
        return Response({"error": "Actor not found."}, status=400)

    movie_data = request.data.get('movie', {})
    movie_data['actors'] = [actor_id]

    movie_serializer = MovieSerializer(data=movie_data)
    if movie_serializer.is_valid():
        movie_instance = movie_serializer.save()
        actor_instance.movies.add(movie_instance)
        return Response(movie_serializer.data, status=201)
    else:
        return Response(movie_serializer.errors, status=400)
