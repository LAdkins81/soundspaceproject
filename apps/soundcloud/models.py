from __future__ import unicode_literals
from ..upload.models import Song
from ..loginandreg.models import User
from django.db import models

class Comment(models.Model):
    user = models.ForeignKey(User)
    song = models.ForeignKey(Song)
    comment = models.TextField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
