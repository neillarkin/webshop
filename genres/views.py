from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import Genre
from records.models import Record


""" Return all Genres and the amount of records in a Genre """
def all_genres(request ):
    genres = Genre.objects.all().order_by('name')
  
    for genre in genres:
        for genre_item in Genre.objects.filter(record__genres=genre.id):
            if genre_item == genre:
                genre.number += 1

    return render(request, "genres.html",  {"genres": genres})
    
""" Get a records and genre using the OneToMany relationship"""
def genres_records(request, id):
    genres = Genre.objects.all()
    genre = Genre.objects.get(id=id)
    genres_records = Record.objects.filter(genres__id=id)
    
    try:
        Genre.objects.get(id=id)
    except Record.DoesNotExist:
        messages.success(request, "Error! Genre does not exist!!")
    except Record.MultipleObjectsReturned:
        messages.success(request, "Error! Only one genre of this name should exist")
    
    
    if Record.objects.filter(genres__id=id):
        pass
    else:
        messages.success(request, "No records in this genre!")
    

    
    return render(request, "genres_records.html", {"genres": genres, "genre": genre, "genres_records": genres_records})