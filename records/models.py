from django.db import models
from artists.models import Artist
from genres.models import Genre

""" A class/model that represents a single record.
    Each line represents columns that will be stored in the database"""
class Record(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, default='0')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, default='0')

    """ This function returns the name of a record as a string"""
    def __str__(self):
        return self.name
