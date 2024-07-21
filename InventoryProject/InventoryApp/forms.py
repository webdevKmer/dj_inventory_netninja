from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'id' : 'Product ID',
            'name' : 'Product Name',
            'sku' : 'SKU',
            'price' : 'Price',
            'quantity' : 'Quantity',
            'supplier' : 'Supplier',
        }
        widgets = {
            'name' : forms.TextInput(attrs={'placeholder': 'e.g : banane', 'class' : 'form-control'}),
            'sku' : forms.TextInput(attrs={'placeholder': 'e.g : SKF345', 'class' : 'form-control'}),
            'price' : forms.NumberInput(attrs={'placeholder': 'e.g : 12.55', 'class' : 'form-control'}),
            'quantity' : forms.NumberInput(attrs={'placeholder': 'e.g : 12', 'class' : 'form-control'}),
            'supplier' : forms.TextInput(attrs={'placeholder': 'e.g : ABC Corp', 'class' : 'form-control'}),
        }