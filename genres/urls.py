# import the urls.py from the main webshop app
from django.conf.urls import url, include
from .views import all_genres, genres_records

urlpatterns = [
    url(r'^$', all_genres, name='genres'),
    url(r'^genres-records/(?P<id>\d+)', genres_records, name='genres_records'),
]