from __future__ import unicode_literals
from django.db import models

class Song(models.Model):
    description = models.TextField(max_length=255, blank=True)
    genre = models.CharField(max_length=45)
    title = models.CharField(max_length=45)
    artist = models.CharField(max_length=45, null=True)
    tags = models.CharField(max_length=45)
    image = models.FileField(upload_to='album_images', max_length=45, null=True)
    song = models.FileField(upload_to='songs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
