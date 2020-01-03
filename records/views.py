from django.shortcuts import render
from .models import Product

"""View function that returns all the products in the database """
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})