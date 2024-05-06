from django.db import models

# En esta parte creamos nuestras tablitas
'''
ID*
Detalles
Status
Lote_ID (FK)

'''


class MateriaPrima(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False )
    supplier = models.CharField(max_length=60, null=False, blank=False)
    united_cost = models.FloatField(null=False, blank=False)
    reception_date = models.DateTimeField(null=False)
    expiration_date = models.DateTimeField(null=False)
    
    def __str__(self):
        return self.name
    
class QualityReport(models.Model):
    details = models.CharField(max_length=150)
    status = models.BooleanField(default=False)
    loteID = models.ForeignKey('lote', null=False, blank=True, on_delete=models.SET_NULL) 
    
