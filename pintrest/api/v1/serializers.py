from rest_framework import serializers
from pintrest.models import Movie,Actor


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'