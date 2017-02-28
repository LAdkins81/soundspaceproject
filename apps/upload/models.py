from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Document(models.Model):
    description = models.TextField(max_length=255, blank=True)
    genre = models.CharField(max_length=45)
    title = models.CharField(max_length=45)
    tags = models.CharField(max_length=45)
    image = models.FileField(upload_to='documents/', null=True)
    song = models.FileField(upload_to='documents/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
