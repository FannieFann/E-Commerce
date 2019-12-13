from django import forms
from .models import Product


class ProductCreateForm(forms.ModelForm):
  class Meta:
    model = Product
    fields = ['category', 'name', 'slug', 'description', 'price', 'availale_date', 'stock', 'image']