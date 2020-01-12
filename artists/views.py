from django.shortcuts import render, redirect, reverse
from .models import Artist
from records.models import Record

"""View function that returns all the records in the database """
def all_artists(request):
    artists = Artist.objects.all()
    return render(request, "artists.html", {"artists": artists})
    
def artists_records(request, id): 
    artists_records = Record.objects.filter(artist_id=id)
    return render(request, "artists_records.html", {"artists_records": artists_records})
    