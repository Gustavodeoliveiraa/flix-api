from rest_framework import serializers
from .models import Movies
from django.db.models import Avg
from genres.serializer import GenreSerializer
from actors.serializer import ActorSerializer


class MoviesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movies
        fields = '__all__'

    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError(
                'A data deve ser maior que 1900'
            )
        return value

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError(
                'O resumo não pode conter mais que 200 caracteres'
            )
        return value


class MoveDetailSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)
    genre = GenreSerializer()
    actors = ActorSerializer(many=True)

    class Meta:
        model = Movies
        fields = [
            'id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume',
        ]

    def get_rate(self, obj):
        rate = obj.review.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)
        return None


class MovieStatsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField()
    total_review = serializers.IntegerField()
    average_stars = serializers.FloatField()
