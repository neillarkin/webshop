from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=254, default='')
    number = models.DecimalField(max_digits=6, decimal_places=0, default=0)
    
    def __str__(self):
        return self.name