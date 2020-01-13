from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from artists.models import Artist
from records.models import Record

# Create your views here.

def do_search(request):
    
    """Get form named q. Data entered in to the form will be filtered"""
    artists = Artist.objects.filter(name__icontains=request.GET['q'])
    records = Record.objects.filter(name__icontains=request.GET['q'])
    
    
    """ Check if objects are present then Return template and dictionary context.
        Else return message and remain on current page
    """
    if artists:
        return render(request, "artists.html", {"artists": artists})  
    elif records:
        return render(request, "records.html", {"records": records}) 
    else:
       messages.error(request, "No results found!")
       return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
