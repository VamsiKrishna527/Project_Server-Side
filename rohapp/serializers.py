from rest_framework  import serializers
from  django.contrib.auth.models import User
from . models import *
class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actors
        fields=('id','name','age','nationality')
        # fields=('id')

class MovieSerializer(serializers.ModelSerializer):
    # actor_id = serializers.IntegerField()
    class  Meta:
        model = Movies
        fields=('title','genre','rating', 'actor_id','release_date','budget','collections')

class PostMovieSerializer(serializers.ModelSerializer):
    actor_id = serializers.IntegerField()
    class Meta:
        model = Movies
        fields = ('title', 'genre', 'rating', 'actor_id')

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()