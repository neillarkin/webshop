from django.shortcuts import render


def index(request):
    """ View that renders the home page"""
    return render(request, "index.html")