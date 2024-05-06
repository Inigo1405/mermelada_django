from django.contrib import admin
from .models import Lot, Machine, Product

# Register your models here.
admin.site.register(Product)
admin.site.register(Lot)
admin.site.register(Machine)