from django.shortcuts import render
from .models import Record

"""View function that returns all the records in the database """
def all_records(request):
    records = Record.objects.all()
    return render(request, "records.html", {"records": records})