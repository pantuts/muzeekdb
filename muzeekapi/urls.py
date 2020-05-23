from django.urls import path, include
from rest_framework import routers

from .views import ArtistView, BandView, TrackView, AlbumView

router = routers.DefaultRouter()
router.register('artists', ArtistView, basename='artist')
router.register('bands', BandView, basename='band')
router.register('tracks', TrackView, basename='track')
router.register('albums', AlbumView, basename='album')

urlpatterns = [
    path('', include(router.urls)),
]
