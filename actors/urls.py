from django.urls import path
from .views import (
    CreateListActorsView,
    ActorRetrieveUpdateDestroyView
)

urlpatterns = [
    path(
        'actors',
        CreateListActorsView.as_view(),
        name='actors_create_list'
    ),

    path(
        'actors/<int:pk>',
        ActorRetrieveUpdateDestroyView.as_view(),
        name='actor_detail_view'
    )
]
