from rest_framework import generics
from .models import Review
from .serializer import ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from app.permission import GlobalDefaultPermission


class ReviewCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
