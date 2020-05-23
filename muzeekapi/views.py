import django_filters
from rest_framework import generics, mixins, status, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from .models import Artist, Band, Track, Album
from .serializers import ArtistSerializer, BandSerializer, TrackSerializer, AlbumSerializer

# Create your views here.

class ArtistFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='full_name', lookup_expr='icontains')
    band = django_filters.CharFilter(field_name='band__name', lookup_expr='icontains', distinct=True)

    class Meta:
        model = Artist
        fields = ['name', 'band']

class BandFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Band
        fields = ['name']

class TrackFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    album = django_filters.CharFilter(field_name='album__title', lookup_expr='icontains')
    artist = django_filters.CharFilter(field_name='artist__full_name', lookup_expr='icontains')
    genre = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Track
        fields = ['title', 'album', 'artist', 'genre']

class AlbumFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Album
        fields = ['title']

class ArtistView(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filterset_class = ArtistFilter
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields = ['full_name', 'created']
    ordering = ['id']
    search_fields = ['full_name', 'band__name']

class BandView(viewsets.ModelViewSet):
    queryset = Band.objects.all()
    serializer_class = BandSerializer
    filterset_class = BandFilter
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['name']

class TrackView(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    filterset_class = TrackFilter
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

class AlbumView(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filterset_class = AlbumFilter
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
