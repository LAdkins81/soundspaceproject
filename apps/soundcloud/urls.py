from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^stream$', index, name='stream'),
    url(r'^stream/logout$', logout, name='logout'),
]
