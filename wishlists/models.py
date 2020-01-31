from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

""" Wishlist class has a Foregin Key of User for a One-To-Many relationsip"""
class Wishlist(models.Model):
    artist_name = models.CharField(max_length=254, default='')
    record_name = models.CharField(max_length=254, default='')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=False)  
    
    def __str__(self):
         return self.artist_name