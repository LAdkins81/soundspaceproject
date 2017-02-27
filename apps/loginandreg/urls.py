from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', index, name='homepage'),
    url(r'^login$', login, name='login'),
    url(r'^register$', register, name='register'),
    url(r'^register/user$', register_user, name='register_user'),
    url(r'^login/user$', login_user, name='login_user'),
]
