from django.shortcuts import render
from .models import Machine, Product, Lot, RawMaterial, QualityReport, Distribution, Lot_RawMaterial

# Create your views here.
def home(request): #se llama 'home'porque es la función de la url que se llama 'home'
    return render(request,'index.html', {})

def login(requets): #Para el html de login
    return render(requets,'login.html',{})

def sign(requets): #Para el html de login
    return render(requets,'sign.html',{})



