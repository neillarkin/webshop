from django.shortcuts import render
from genres.models import Genre

def index(request):
    """ View that renders the home page"""
    genres = Genre.objects.all()
    return render(request, "index.html", {"genres": genres})