from django.shortcuts import render, redirect, get_object_or_404
from .models import ProductionLine, Flavor, Product, Lot, RawMaterial, Distribution
from .forms import FlavorForm, ProductionLineUpdateForm, ProductForm

# Create your views here.
def home(request): #se llama 'home'porque es la función de la url que se llama 'home'
    return render(request,'index.html', {})

def login(requets): #Para el html de login
    return render(requets,'login.html',{})

def list_products(request):
    products = Product.objects.all() #NO SE TE OLVIDE NAOMI: Para traerlos todos
    return render(request,'products.html',{'products': products}) #Se pone como diccionario porque los guardamos como json


def production(request):
    lines = ProductionLine.objects.all()
    return render(request, 'production.html', {'lines': lines})

def production_update(request):
    if request.method == 'POST':
        line_id = request.POST.get('line_id')
        line = get_object_or_404(ProductionLine, id=line_id)
        form = ProductionLineUpdateForm(request.POST, instance=line)
        if form.is_valid():
            form.save()
            return redirect('production_status')  # Redirect back to the production status page
    else:
        lines = ProductionLine.objects.all()
        return render(request, 'production_update.html', {'lines': lines})  # Use the same template or a different one if needed



def manage_products(request):
    if request.method == 'POST':
        if 'delete' in request.POST:
            product_id = request.POST.get('delete')
            product = get_object_or_404(Product, id=product_id)
            product.delete()
            return redirect('manage_products')
        else:
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('manage_products')
    else:
        products = Product.objects.all()
        form = ProductForm()
    return render(request, 'manage_products.html', {'products': products, 'form': form})



def flavor_crud(request, id=None):
    if request.method == 'POST':
        if 'create_or_update' in request.POST:
            if id:
                flavor = get_object_or_404(Flavor, id=id)
                form = FlavorForm(request.POST, instance=flavor)
            else:
                form = FlavorForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('flavor_crud')
        elif 'delete' in request.POST:
            flavor = get_object_or_404(Flavor, id=id)
            flavor.delete()
            return redirect('flavor_crud')

    flavors = Flavor.objects.all()
    form = FlavorForm(instance=get_object_or_404(Flavor, id=id) if id else None)
    return render(request, 'flavor_crud.html', {'flavors': flavors, 'form': form})


# ToDo: RawMaterial, Lot, distribution
def lot(request):
    lots = Lot.objects.all() 
    return render(request,'lot.html',{'lots': lots})


def rawMaterial(request):
    materials = RawMaterial.objects.all() 
    return render(request,'rawMaterial.html',{'rawMaterials': materials})

def distribution(request):
    distributions = Distribution.objects.all() 
    return render(request,'distribution.html',{'distributions': distributions})