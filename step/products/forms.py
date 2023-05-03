from django import forms
from .models import Products

class AddProductForm(forms.Form):
    product_name = forms.CharField()
    product_price = forms.IntegerField()
    product_category = forms.ChoiceField(choices=Products.CATEGORY_CHOICES)
    product_image = forms.ImageField()
    items_remaining = forms.IntegerField()


    class Meta:
        model = Products
        fields = ['product_name', 'product_price', 'product_category', 'product_image', 'items_remaining']
