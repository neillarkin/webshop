from django.shortcuts import render
from records.models import Record

# Create your views here.
def do_search(request):
    """Get form named q. Data entered in to the form will be filtered"""
    records = Record.objects.filter(name__icontains=request.GET['q'])
    """ Return template and dictionary context of records"""
    return render(request, "records.html", {"records": records})
