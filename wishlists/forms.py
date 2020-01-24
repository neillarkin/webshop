from django import forms
from .models import Wishlist


class WishForm(forms.ModelForm):

    class Meta:
        model = Wishlist  #uses Order model from models.py class
        fields = (
            'artist_name', 'record_name'
        )