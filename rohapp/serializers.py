from rest_framework  import serializers
#from  django.contrib.auth.models import User,
from . models import *
class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actors
        fields=('id','name','age','nationality')

class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True, required=False)
    class  Meta:
        model = Movies
        fields=('title','genre','rating', 'actors')