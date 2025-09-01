from django import forms
from.models import ProductListings




class ProductListingForm(forms.ModelForm):
    class Meta:
        model = ProductListings

        fields = ['title', 'description', 'price', 'image', 'location']