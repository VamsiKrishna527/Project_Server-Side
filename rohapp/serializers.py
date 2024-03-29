from rest_framework  import serializers
#from  django.contrib.auth.models import User,
from . models import *
class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actors
        fields=('id','name','age','nationality')
        # fields=('id')

class MovieSerializer(serializers.ModelSerializer):
    actor_id = serializers.IntegerField()
    class  Meta:
        model = Movies
        fields=('title','genre','rating', 'actor_id')
    def create(self, validated_data):
        actor_id = validated_data.pop('actor_id')
        movie_instance = Movies.objects.create(actor_id=actor_id, **validated_data)
        return movie_instance