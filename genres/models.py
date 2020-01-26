from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=15, default='')
    number = models.DecimalField(max_digits=6, decimal_places=0, default=0)
    
    def __str__(self):
        return self.name
