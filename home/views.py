from django.shortcuts import render
from genres.models import Genre

""" View that renders the home page"""
def index(request):
    genres = Genre.objects.all().order_by('name')
    return render(request, "index.html", {"genres": genres})