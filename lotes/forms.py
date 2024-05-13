from django import forms
from .models import Flavor, ProductionLine, Product, Profile, Lot
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
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


class LotForm(forms.ModelForm):
    class Meta:
        model = Lot
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Calcula el valor de production_Cost si el formulario está vinculado a una instancia existente
        if self.instance.pk:
            self.fields['production_Cost'].widget.attrs['readonly'] = True
            self.fields['production_Cost'].initial = self.instance.stock * 19
        else:
            # Si es un nuevo formulario, production_Cost será calculado después de enviar el formulario
            self.fields['production_Cost'].widget = forms.HiddenInput()
            self.fields['user_ID'].widget = forms.HiddenInput()

    def clean(self):
        cleaned_data = super().clean()
        # Calcula el valor de production_Cost si es un formulario nuevo
        if not self.instance.pk:
            cleaned_data['production_Cost'] = cleaned_data.get('stock') * 19
        return cleaned_data
    
    

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password'
        )