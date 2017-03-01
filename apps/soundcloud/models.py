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

class RelationshipManager(models.Manager):
    def follow(self, info, **kwargs):
        following = User.objects.get(id=info['followingid'])
        follower = User.objects.get(id=info['followerid'])
        Relationship.objects.get_or_create(following=following, follower=follower)
        return {'success': 'Followed!'}

    def unfollow(self, info, **kwargs):
        unfollow = User.objects.get(id=info['unfollowid'])
        follower = User.objects.get(id=info['followerid'])
        Relationship.objects.get(following=unfollow, follower=follower).delete()
        return {'success': 'Unfollowed!'}

class Relationship(models.Model):
    following = models.ForeignKey(User, related_name='user_following')
    follower = models.ForeignKey(User, related_name='user_followers')
    created_at = models.DateTimeField(auto_now_add=True)

    objects = RelationshipManager()
