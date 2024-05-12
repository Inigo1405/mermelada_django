from django.shortcuts import render, redirect, get_object_or_404
from .models import ProductionLine, Flavor, Product
from .forms import FlavorForm, ProductionLineUpdateForm, ProductForm

def home(request): #se llama 'home'porque es la función de la url que se llama 'home'
    return render(request,'index.html', {})

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