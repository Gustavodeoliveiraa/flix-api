from django.urls import path
from .views import (
    MovieCreateList,
    MovieRetrieveUpdateDestroyView
)

urlpatterns = [
    path(
        'movies/',
        MovieCreateList.as_view(),
        name='movie_create_list'
    ),

    path(
        'movies/<int:pk>/',
        MovieRetrieveUpdateDestroyView.as_view(), 
        name='movie_detail_view'
    ),
]
