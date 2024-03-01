from rest_framework import serializers
from .models import Actors


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actors
        fields = '__all__'