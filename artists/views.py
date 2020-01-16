from django.shortcuts import render, redirect, reverse
from .models import Artist
from records.models import Record
from genres.models import Genre

"""View function that returns all the records in the database """
def all_artists(request):
    artists = Artist.objects.all()
    genres = Genre.objects.all()
    return render(request, "artists.html", {"artists": artists, "genres": genres})
    
def artists_records(request, id):
    artist = Artist.objects.get(id=id)
    artists_records = Record.objects.filter(artist_id=id)
    return render(request, "artists_records.html", {"artist": artist, "artists_records": artists_records})