from django.shortcuts import render
from .models import Record
from genres.models import Genre

"""View function that returns all the records in the database """
def all_records(request):
    records = Record.objects.all()
    genres = Genre.objects.all()
    return render(request, "records.html",  {"records": records, "genres": genres})
