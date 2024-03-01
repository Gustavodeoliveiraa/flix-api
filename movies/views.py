from rest_framework import generics
from .models import Movies
from .serializer import MoviesSerializer
from rest_framework.permissions import IsAuthenticated
from app.permission import GlobalDefaultPermission


class MovieCreateList(generics.ListCreateAPIView):

    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
