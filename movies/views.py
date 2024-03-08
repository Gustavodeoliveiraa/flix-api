from rest_framework import generics, views, response, status
from .models import Movies
from django.db.models import Count, Avg
from .serializer import (
    MoviesSerializer, MovieStatsSerializer, MoveDetailSerializer
)
from rest_framework.permissions import IsAuthenticated
from app.permission import GlobalDefaultPermission
from review.models import Review


class MovieCreateList(generics.ListCreateAPIView):

    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movies.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MoveDetailSerializer
        return MoviesSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movies.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MoveDetailSerializer
        return MoviesSerializer


class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movies.objects.all()

    def get(self, request):
        total_movies = self.queryset.count()

        movies_by_genre = self.queryset.values(
            'genre__name'
        ).annotate(count=Count('id'))

        total_review = Review.objects.count()

        average_stars = round(
            Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars'], 2
        )

        movie_stats = {
            'total_movies': total_movies,
            'movies_by_genre': movies_by_genre,
            'total_review': total_review,
            'average_stars': average_stars
        }

        serializer = MovieStatsSerializer(data=movie_stats)
        serializer.is_valid(raise_exception=True)  # valida os dados e se n for da um exception

        return response.Response(
            data=serializer.validated_data,
            status=status.HTTP_200_OK
        )
