from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from artists.models import Artist
from records.models import Record
from collections import Counter
# Create your views here.

def do_search(request):
   
    """Get form named q. Data entered in to the form will be filtered"""
    artists = Artist.objects.filter(name__icontains=request.GET['q'])
    records = Record.objects.filter(name__icontains=request.GET['q'])
    artist_results = []
    records_results = []
    
    """ Check if objects are present then Return template and dictionary context.
        Else return message and remain on current page
    """
    if artists:
        for x in artists:
            artist_results.append(artists)
        len(artist_results)
        messages.success(request, str(len(artist_results)) + " artists found!")
        return render(request, "artists.html", {"artists": artists,"records": records })  
    elif records:
        for x in records:
            records_results.append(records)
        len(records_results)
        messages.success(request, str(len(records_results)) + " records found!")
        return render(request, "records.html", {"records": records}) 
    else:
       messages.error(request, "No results found!")
       return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
