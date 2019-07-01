from django.conf.urls import url
from .views import allblogs, detail, create_post

urlpatterns = [

    url(r'^create/$', create_post, name='create'),
    url(r'^(?P<id>\d+)/$', detail, name='detail'),
    url(r'^$', allblogs, name='home'),
]
