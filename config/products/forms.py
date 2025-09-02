from django import forms
from.models import ProductListings


# ------------------ Product Form ------------------

# A form to create or update product listings using Django's ModelForm
class ProductListingForm(forms.ModelForm):
    class Meta:
        model = ProductListings

        # Only include these fields in the form (seller handled separately)
        fields = ['title', 'description', 'price', 'image', 'location', 'category']