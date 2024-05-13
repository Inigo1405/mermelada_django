from django.shortcuts import render, redirect, get_object_or_404
from .models import ProductionLine, Flavor, Product, Lot, RawMaterial, Distribution
from .forms import FlavorForm, ProductionLineUpdateForm, ProductForm, SignUpForm, LotForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def home(request):
    return render(request, 'index.html', {})

def production(request):
    lines = ProductionLine.objects.all()
    return render(request, 'production.html', {'lines': lines})

@login_required
def production_update(request):
    if request.method == 'POST':
        line_id = request.POST.get('line_id')
        line = get_object_or_404(ProductionLine, id=line_id)
        form = ProductionLineUpdateForm(request.POST, instance=line)
        if form.is_valid():
            form.save()
            return redirect('production_status')
    else:
        lines = ProductionLine.objects.all()
        return render(request, 'production_update.html', {'lines': lines})

@login_required
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

@login_required
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

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if hasattr(user, 'profile') and user.profile.is_manager:
                    return redirect('manager_dashboard')
                else:
                    return redirect('customer_dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid login attempt. Please try again.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')  
            return redirect('customer_dashboard') 
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def view_production(request):
    if hasattr(request.user, 'profile') and request.user.profile.is_manager:
        return redirect('manager_dashboard')
    lines = ProductionLine.objects.all()
    return render(request, 'production.html', {'lines': lines})

@login_required
def view_products_and_flavors(request):
    if hasattr(request.user, 'profile') and request.user.profile.is_manager:
        return redirect('manager_dashboard')
    products = Product.objects.all()
    flavors = Flavor.objects.all()
    return render(request, 'products_flavors.html', {'products': products, 'flavors': flavors})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@login_required
def manager_dashboard(request):
    if hasattr(request.user, 'profile') and request.user.profile.is_manager:
        return render(request, 'manager_dashboard.html', {})
    else:
        return redirect('home')

@login_required
def customer_dashboard(request):
    if hasattr(request.user, 'profile') and request.user.profile.is_manager:
        return redirect('manager_dashboard')
    return render(request, 'customer_dashboard.html')

# ToDo: RawMaterial, Lot, distribution
@login_required
def lot(request):
    lots = Lot.objects.all() 
    user_profile = request.user.profile
    context = {'lots': lots, 'user_profile': user_profile}
    return render(request,'lot.html', context)

@login_required
def rawMaterial(request):
    materials = RawMaterial.objects.all() 
    return render(request,'rawMaterial.html',{'rawMaterials': materials})

@login_required
def distribution(request):
    distributions = Distribution.objects.all() 
    return render(request,'distribution.html',{'distributions': distributions})


@login_required
def tu_vista(request):
    if request.method == 'POST':
        form = LotForm(request.POST)
        if form.is_valid():
            lot = form.save(commit=False)
            # Asigna el perfil del usuario actual al lote antes de guardarlo
            lot.user_ID = request.user.profile
            lot.save()
            # Redirige a donde quieras
            return redirect('xd')
    else:
        form = LotForm()
    return render(request, 'createLot.html', {'form': form})