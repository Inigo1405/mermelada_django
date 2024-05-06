from django.db import models

# En esta parte creamos nuestras tablita

class RawMaterials(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False )
    supplier = models.CharField(max_length=60, null=False, blank=False)
    united_cost = models.FloatField(null=False, blank=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    expiration_date = models.DateTimeField(null=False)
    
    def __str__(self):
        return self.name
    
class QualityReport(models.Model):
    details = models.CharField(max_length=150)
    status = models.BooleanField(default=False)
    loteID = models.ForeignKey('lote', null=False, blank=True, on_delete=models.SET_NULL) 
    
    def __str__(self):
        return self.details
    
class Distribution(models.Model):
    loteID = models.ForeignKey('lote', null=False, blank=True, on_delete=models.SET_NULL)
    distribution_date = models.DateTimeField(null=False)
    destination =  models.CharField(max_length=100, null=False)
    
    def __str__(self):
        return self.destination

class RawMaterialsLote(models.Model):
    loteID = models.ForeignKey('lote', null=False, blank=True, on_delete=models.SET_NULL)
    rawMaterialID =  models.ForeignKey('RawMaterials', null=False, blank=True, on_delete=models.SET_NULL)
    quantity = models.FloatField(null=False)
    
    def __str__(self):
        return self.quantity
    
