from django.shortcuts import render
from .models import RawMaterials, QualityReport, RawMaterialsLote, Distribution 

# Create your views here.
def home(request): #se llama 'home'porque es la función de la url que se llama 'home'
    return render(request,'index.html', {})

