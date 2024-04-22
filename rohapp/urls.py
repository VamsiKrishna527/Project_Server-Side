from django.urls import path
from .views import ActorsList, CreateActorView, MoviesList, home, CreateMovieView, ActorMovieDeleteView, MovieUpdateView, UserRegistrationAPIView, UserLoginAPIView, UserLogoutAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('',home,name='Home'),
    path('actors/', ActorsList.as_view(), name='actors-list'),
    path('movies/', MoviesList.as_view(), name='movies-list'),
    path('movies/create/',CreateMovieView.as_view(), name='create_movie_for_actor'),
    path('movies/delete/', ActorMovieDeleteView.as_view(), name="actor_movie_delete"),
    path('movies/update/',MovieUpdateView.as_view(),name='update_movie'),
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='api_login'),
    path('logout/', UserLogoutAPIView.as_view(), name='api_logout'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('actors/create/', CreateActorView.as_view())
]