from rest_framework  import serializers
from  django.contrib.auth.models import User
from . models import *
from django.contrib.auth import authenticate

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
    email = serializers.EmailField()
    name = serializers.CharField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'name']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                data['user'] = user
                return data
            else:
                raise serializers.ValidationError("Unable to log in with provided credentials.")
        else:
            raise serializers.ValidationError("Must include 'username' and 'password'")