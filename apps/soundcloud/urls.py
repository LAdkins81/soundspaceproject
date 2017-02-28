from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^stream$', index, name='stream'),
    url(r'^stream/logout$', logout, name='logout'),
    url(r'^update/(?P<id>\d+)$', update, name='update'),
    url(r'^user/(?P<id>\d+)$', user, name='user'),
    url(r'^stream/addcomment$', create_comment, name='addcomment'),
    url(r'^stream/deletecomment$', delete_comment, name='deletecomment'),
]
