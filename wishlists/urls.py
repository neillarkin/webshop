""" import the urls.py from the main webshop app """
from django.conf.urls import url, include
from .views import all_wishes, edit_wish

urlpatterns = [
    url(r'^$', all_wishes, name='wishes'),
    
]
