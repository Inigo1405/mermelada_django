from django import forms
from .models import Flavor, ProductionLine, Product, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FlavorForm(forms.ModelForm):
    class Meta:
        model = Flavor
        fields = ['name', 'description']

class ProductionLineUpdateForm(forms.ModelForm):
    class Meta:
        model = ProductionLine
        fields = ['progresField', 'is_available']
        

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'netContent', 'flavor_id']
        widgets = {
            'flavor_id': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'netContent': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')