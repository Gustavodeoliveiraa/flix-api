from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Actors
from .serializer import ActorSerializer
from app.permission import GlobalDefaultPermission


class CreateListActorsView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Actors.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Actors.objects.all()
    serializer_class = ActorSerializer
