from django.urls import path
from .views import (
    MovieCreateList,
    MovieRetrieveUpdateDestroyView,
    MovieStatsView
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
    path('movies/stats/', MovieStatsView.as_view(), name='movie_stats_view')
]
