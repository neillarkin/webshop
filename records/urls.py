""" import the urls.py from the main webshop app """
from django.conf.urls import url, include
from .views import all_products

urlpatterns = [
    url(r'^$', all_products, name='products'),
]