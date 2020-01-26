from django.shortcuts import render
from .models import Genre
from records.models import Record
from collections import Counter

# Create your views here.
def all_genres(request ):
    genres = Genre.objects.all()
    records = Record.objects.all()
    
    records_genres = []
 
    
    for genre in genres:
        records_genres.append(Genre.objects.filter(record__genres=genre.id))
        for record in records_genres:
            for x in record:
                if x == genre:
                    genre.number = genre.number + 1
        
    return render(request, "genres.html",  {"genres": genres})
    
""" Get a records and genre using the OneToMany relationship"""
def genres_records(request, id):
    genres = Genre.objects.all()
    genre = Genre.objects.get(id=id)
    genres_records = Record.objects.filter(genres__id=id)
    return render(request, "genres_records.html", {"genres": genres, "genre": genre, "genres_records": genres_records})