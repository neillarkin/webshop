from django.shortcuts import render
from django.contrib import messages
from .models import Record
from genres.models import Genre

"""View function that returns all the records in the database """
def all_records(request):
    genres = Genre.objects.all()
    records = Record.objects.all()
    
    try:
        records = Record.objects.all()
    except Record.DoesNotExist:
        messages.success(request, "No Records in store!")
    except Record.MultipleObjectsReturned:
        records
    
    return render(request, "records.html",  {"records": records, "genres": genres})


