# import the urls.py from the main webshop app
from django.conf.urls import url, include
from .views import all_records

urlpatterns = [
    url(r'^$', all_records, name='records'),
]