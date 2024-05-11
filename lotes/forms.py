from django import forms
from .models import Flavor, ProductionLine

class FlavorForm(forms.ModelForm):
    class Meta:
        model = Flavor
        fields = ['name', 'description']

class ProductionLineUpdateForm(forms.ModelForm):
    class Meta:
        model = ProductionLine
        fields = ['progresField', 'is_available']