from rest_framework import serializers
from .models import Track, Album, Artist, Band


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    release_date = serializers.DateTimeField(format='%Y-%m-%d', input_formats=['%Y-%m-%d'])

    class Meta:
        model = Album
        fields = '__all__'

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class BandSerializer(serializers.ModelSerializer):
    artists = serializers.StringRelatedField(many=True)

    class Meta:
        model = Band
        fields = ['name', 'artists', 'created', 'modified']
