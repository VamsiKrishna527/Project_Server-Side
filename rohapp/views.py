from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework import generics
from .models import Actors, Movies
from .serializers import ActorSerializer, MovieSerializer

def home(request):
    return HttpResponse("Welcome to the API!")


class ActorsList(generics.ListCreateAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorSerializer

class MoviesList(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer



