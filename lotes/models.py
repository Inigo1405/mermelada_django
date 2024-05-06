from django.db import models

# Create your models here.
class Machine(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    status = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) :
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=60)
    netContent = models.TextField()
    flavor = models.CharField(max_length=60)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) :
        return self.name


class Lot(models.Model):
    stock = models.IntegerField()
    sell_Cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    production_Cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    product_ID = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, blank=True)
    delivery_Date = models.DateTimeField(null=True)
    expiry_Date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) :
        return self.created_at


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
    
    
class QualityReport(models.Model):
    description = models.CharField(max_length=150)
    status = models.BooleanField(default=False)
    lot_ID = models.ForeignKey('Lot', null=True, blank=True, on_delete=models.SET_NULL) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.created_at
    
    
class Distribution(models.Model):
    destination = models.CharField(max_length=70)
    status = models.BooleanField(default=True)
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
        return self.quantity