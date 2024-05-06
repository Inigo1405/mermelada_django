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
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, blank=True)
    expiryDate = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) :
        return self.created_at
    