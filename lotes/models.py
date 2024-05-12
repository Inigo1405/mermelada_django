from django.db import models
from django.contrib.auth.models import UserManager
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]
class ProductionLine(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    progresField = models.DecimalField(max_digits=3, decimal_places=0, default=0, validators=PERCENTAGE_VALIDATOR)
    is_available = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

    def current_machine(self):
        if self.progresField == 100:
            return 'Finished Machine'
        elif self.progresField > 80 and self.progresField <= 99:
            return 'Labeling and Sealing Machine'
        elif self.progresField > 60 and self.progresField <= 80:
            return 'Filling'
        elif self.progresField > 40 and self.progresField <= 60:
            return 'Cooking Kettle'
        elif self.progresField > 20 and self.progresField <= 40:
            return 'Fruit Crusher'
        elif self.progresField > 0 and self.progresField <= 20:
            return 'Fruit Washer'
        else:
            return 'Not started'

class Flavor(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    
    def __str__(self) :
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=60)
    netContent = models.TextField()
    flavor_id = models.ForeignKey('Flavor', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) :
        return self.name


class Lot(models.Model):
    stock = models.IntegerField()
    production_Cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    qualityStatus = models.BooleanField(default=True)
    expiry_Date = models.DateTimeField(null=False)
    machine_id = models.ForeignKey('ProductionLine', on_delete=models.SET_NULL, null=True, blank=True)
    product_ID = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) :
        return self.created_at.strftime("%Y-%m-%d %H:%M:%S")


class RawMaterial(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False )
    supplier = models.CharField(max_length=60, null=False, blank=False)
    united_cost = models.FloatField(null=False, blank=False)
    expiry_Date = models.DateTimeField(null=False)
    is_available = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
class Distribution(models.Model):
    destination = models.CharField(max_length=70)
    status = models.BooleanField(default=True)
    sell_Cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    lot_ID = models.ForeignKey('Lot', null=True, blank=True, on_delete=models.SET_NULL) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.destination
    
    
class Lot_RawMaterial(models.Model):
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    lot_ID = models.ForeignKey('Lot', null=True, blank=True, on_delete=models.SET_NULL) 
    rowMaterial_ID = models.ForeignKey('RawMaterial', null=True, blank=True, on_delete=models.SET_NULL) 
    
    def __str__(self):
        return str(self.id)
    
    
class CustomUser(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail addres")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
        