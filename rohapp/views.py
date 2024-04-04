
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Actors, Movies
from .serializers import ActorSerializer, MovieSerializer, PostMovieSerializer
from rest_framework.decorators import api_view


def home(request):
    return HttpResponse("Welcome to the API!")


class ActorsList(generics.ListCreateAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorSerializer

class MoviesList(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

#@api_view(['POST'])
# def create_movie_for_actor(request):
#     actor_id = request.data.get('actor_id')
#     actor_instance = Actors.objects.get(pk=actor_id)

#     if not actor_instance:
#         return Response({"error": "Actor not found."}, status=400)

#     movie_data = request.data.get('movie', {})
#     movie_data['actors'] = [actor_id]

#     movie_serializer = MovieSerializer(data=movie_data)
#     if movie_serializer.is_valid():
#         movie_instance = movie_serializer.save()
#         actor_instance.movies.add(movie_instance)
#         return Response(movie_serializer.data, status=201)
#     else:
#         return Response(movie_serializer.errors, status=400)

class CreateMovieView(generics.CreateAPIView):
    serializer_class = PostMovieSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class ActorMovieDeleteView(generics.DestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

    def delete(self, request, *args, **kwargs):
        movie_name = request.data.get('movie_name')  # pass the movie name in the request data
        actor_id = request.data.get('actor_id')
        print(movie_name,actor_id)
        try:
            movie = self.queryset.get(title=movie_name, actor_id=actor_id)
            movie.delete()
            return Response({"message": "Movie details deleted from actor successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Movies.DoesNotExist:
            return Response({"error": "Movie not found for the actor."}, status=status.HTTP_404_NOT_FOUND)
        

class MovieUpdateView(generics.UpdateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

    def put(self, request, *args, **kwargs):
        movie_name = request.data.get('movie_name')
        actor_id = request.data.get('actor_id')
        new_movie_data = request.data.get('new_movie_data')  # updated movie data

        try:
            # Find the movie based on provided movie name and actor ID
            movie = self.queryset.get(title=movie_name, actor_id=actor_id)
        except Movies.DoesNotExist:
            return Response({"error": "Movie not found for the actor."}, status=status.HTTP_404_NOT_FOUND)

        # Update the movie details with the new data
        serializer = self.get_serializer(movie, data=new_movie_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)