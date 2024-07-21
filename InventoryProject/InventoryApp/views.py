from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

# Create your views here.

def home(request):
    return render(request, 'InventoryApp/home.html')

def product_list_view(request):
    products = Product.objects.all()
    context = {
        'products' : products
    }
    return render(request, 'InventoryApp/index.html', context)

def product_create_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else :
        form = ProductForm()
    context = {
        'form' : form
    }
    return render(request, 'InventoryApp/product_create.html', context)

def product_update_view(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance = product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else :
        form = ProductForm(instance = product)
    context = {
        'form' : form
    }
    return render(request, 'InventoryApp/product_create.html', context)

def confirm_delete_view(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'product' : product
    }
    return render(request, 'InventoryApp/product_delete_confirmation.html', context)

def product_delete_view(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect('product_list')
