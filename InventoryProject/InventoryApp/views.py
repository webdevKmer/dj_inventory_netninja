from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'InventoryApp/home.html')

def index(request):
    return render(request, 'InventoryApp/index.html')