from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^create$', create, name='create'),
    url(r'^add_playlist/(?P<id>\d+)$', add_playlist, name='add_playlist'),
    url(r'^create_playlist$', create_playlist, name='create_playlist'),
    url(r'^delete_playlist_song/(?P<id>\d+)$', delete_playlist_song, name='delete_playlist_song'),
    url(r'^playlist_info/(?P<id>\d+)$', playlist_info, name='playlist_info'),
    url(r'^repost/(?P<id>\d+)$', repost, name='repost'),
    url(r'^remove_repost/(?P<id>\d+)$', remove_repost, name='remove_repost'),
]
