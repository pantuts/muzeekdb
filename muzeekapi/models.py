from django.db import models
from rest_framework.exceptions import ParseError
from rest_framework import status

from utils import create_dir

# Create your models here.

class Track(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    track_number = models.PositiveSmallIntegerField(null=True, blank=True)
    album = models.ForeignKey('Album', related_name='tracks', on_delete=models.CASCADE, null=True, blank=True)
    band = models.ForeignKey('Band', on_delete=models.SET_NULL, null=True, blank=True)
    artist = models.ForeignKey('Artist', on_delete=models.SET_NULL, null=True, blank=True)
    genre = models.CharField(max_length=100, default='', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['track_number']

    def save(self, *args, **kwargs):
        if not self.band and not self.artist:
            raise ParseError(detail='Band or Artist should not be empty', code=status.HTTP_400_BAD_REQUEST)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.track_number}: {self.title}'

class Album(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    release_date = models.DateTimeField(default='', blank=True)
    album_art = models.URLField(default='', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title.title()}'

class Artist(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=30, default='', blank=True)
    full_name = models.CharField(max_length=85, default='', blank=True)
    band = models.ManyToManyField('Band', related_name='artists', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.full_name and self.first_name:
            self.full_name = ' '.join(list(filter(None, [self.first_name, self.last_name])))
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.full_name.title()}'

class Band(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name.title()}'
