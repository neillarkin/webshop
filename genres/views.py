from django.shortcuts import render
from .models import Genre
from records.models import Record

# Create your views here.
def all_genres(request):
    genres = Genre.objects.all()
    records = Record.objects.all()
    return render(request, "genres.html", {"genres": genres, "records": records})
    

def genres_records(request, id):
    genres = Genre.objects.all()
    genre = Genre.objects.get(id=id)
    genres_records = Record.objects.filter(genres__id=id)
    return render(request, "genres_records.html", {"genres": genres, "genre": genre, "genres_records": genres_records})