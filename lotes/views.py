from django.shortcuts import render
from .models import Product

# Create your views here.
# Create your views here.
def home(request): #se llama 'home'porque es la función de la url que se llama 'home'
    return render(request,'index.html', {})

def login(requets): #Para el html de login
    return render(requets,'login.html',{})

def list_products(request):
    products = Product.objects.all() #NO SE TE OLVIDE NAOMI: Para traerlos todos
    return render(request,'products.html',{'products': products}) #Se pone como diccionario porque los guardamos como json




