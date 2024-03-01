from django.urls import path
from .views import GenreCreateListView, GenreRetrieveUpdateView

urlpatterns = [
     path(
            'genres/',
            GenreCreateListView.as_view(),
            name='-create-list'
        ),
     path(
            'genres/<int:pk>/',
            GenreRetrieveUpdateView.as_view(),
            name='genre-detail-view'
        ),
]
