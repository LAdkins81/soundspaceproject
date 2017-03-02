from __future__ import unicode_literals
from django.db import models
from ..loginandreg.models import User

class Song(models.Model):
    user = models.ForeignKey(User, null=True)
    description = models.TextField(max_length=255, blank=True)
    genre = models.CharField(max_length=45)
    title = models.CharField(max_length=45)
    artist = models.CharField(max_length=45)
    tags = models.ManyToManyField('Tag', related_name='songs', blank=True)
    image = models.FileField(upload_to='album_images', max_length=45, null=True)
    song = models.FileField(upload_to='songs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name= models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Playlist(models.Model):
    name = models.CharField(max_length=45)
    genre = models.CharField(max_length=45, null=True )
    description = models.TextField(max_length=45, null=True)
    songs = models.ManyToManyField(Song, related_name="song_playlists")
    user= models.ForeignKey(User, related_name="user_playlists")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Repost(models.Model):
    post= models.ForeignKey(Song, related_name='song_reposts')
    user= models.ForeignKey(User, related_name='user_reposts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
