from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Artist
from records.models import Record
from genres.models import Genre

"""View function that returns all the records in the database """
def all_artists(request):
    artists = Artist.objects.all().order_by('name')
    genres = Genre.objects.all()
    return render(request, "artists.html", {"artists": artists, "genres": genres})
    
def artists_records(request, id):
    genres = Genre.objects.all()
    artist = Artist.objects.get(id=id)
    artists_records = Record.objects.filter(artist_id=id).order_by('name')
    
    try:
         artist = Artist.objects.get(id=id)
    except Record.DoesNotExist:
        messages.success(request, "Artist does not exist!!")
    
    
    if Record.objects.filter(artist_id=id):
        pass
    else:
        messages.success(request, "No Records for this Artist!")
    

    return render(request, "artists_records.html", {"genres": genres, "artist": artist, "artists_records": artists_records})