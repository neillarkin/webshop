from django.shortcuts import render
from wishlists.models import Wishlist
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django import forms
from .forms import WishForm
# def all_wishes(request):
#     user = User.objects.get(email=request.user.email)
#     artists_records = Wishlist.objects.filter(user_id=user.id)
#     wishlist = Wishlist.objects.all()
#     return render(request, "profile.html",  {"profile": user, "wishlist":wishlist})


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
    else:
        wishlist_form = WishForm()
    wishes = Wishlist.objects.filter(user_id=request.user.id)
    return redirect(reverse('profile'))
          
def edit_wish(request, id):
    wish = Wishlist.objects.get(id=id)
    return render(request, 'edit_wishlists.html', {'wish': wish})
    
def update_wish(request):
    return render(request, 'profile.html')
    