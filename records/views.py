from django.shortcuts import render
from django.contrib import messages
from .models import Record
from genres.models import Genre

"""View function that returns all the records in the database """
def all_records(request):
    genres = Genre.objects.all().order_by('name')
    records = Record.objects.all().order_by('name')
   
    if Record.objects.all():
        pass
    else:
        messages.success(request, "No Records in stock!")
    
    return render(request, "records.html",  {"records": records, "genres": genres})
