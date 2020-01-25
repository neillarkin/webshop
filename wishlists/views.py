from django.shortcuts import render
from django.contrib import messages
from wishlists.models import Wishlist
from django.shortcuts import render, redirect, reverse
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django import forms
from .forms import WishForm


""" Add a new wish row to the Wishlist table object """
def add_wish(request):
    user = request.user
    if request.method == "POST":
        wishlist_form = WishForm(request.POST)
        if wishlist_form.is_valid():
            wishlist = Wishlist()
            wishlist.artist_name = request.POST.get('artist_name')
            wishlist.record_name = request.POST.get('record_name')
            wishlist.user_id = user.id
            wishlist.save()
            messages.success(request, "Record added to wishlist!")
    else:
        wishlist_form = WishForm()
    wishes = Wishlist.objects.filter(user_id=request.user.id)
    return redirect(reverse('profile'))

""" Edit wish using current wish row id """
def edit_wish(request, id):
    wish = Wishlist.objects.get(id=id)
    return render(request, 'edit_wishlists.html', {'wish': wish})

""" Update a wish row after validating form fields"""
def update_wish(request, id):
    if request.method == "POST":
        wishlist_form = WishForm(request.POST)
        if wishlist_form.is_valid():
            wish = Wishlist.objects.get(id=id)
            wish.artist_name = request.POST.get('artist_name')
            wish.record_name = request.POST.get('record_name')
            wish.save()
            messages.success(request, "Record updated!")
    else:
        wishlist_form = WishForm()
    return redirect(reverse('profile'))

""" Delete wish roww from Wishlist table"""
def remove_wish(request, id):
    wish = Wishlist.objects.get(id=id)
    wish.delete()
    messages.success(request, "Record removed from wishlist!")
    return redirect(reverse('profile'))