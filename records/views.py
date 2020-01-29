from django.shortcuts import render
from .models import Record
from genres.models import Genre

"""View function that returns all the records in the database """
def all_records(request):
    genres = Genre.objects.all()
    records = Record.objects.all()
    return render(request, "records.html",  {"records": records, "genres": genres})
