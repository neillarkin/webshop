from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=15, default='')
    
    def __str__(self):
        return self.name
