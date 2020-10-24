from .models import ProductInformation
from django import forms


class ProductForm(forms.ModelForm):

    class Meta:
        model = ProductInformation
        fields = ('product_name', 'price', 'quantity', 'status', 'product_image')
