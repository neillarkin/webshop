""" import the urls.py from the main webshop app """
from django.conf.urls import url, include
from .views import all_artists, artists_records

urlpatterns = [
    url(r'^$', all_artists, name='artists'),
    url(r'^artists-records/(?P<id>\d+)', artists_records, name='artists_records'),
]

#  url(r'^artists-records', artists_records, name='artists_records'),
