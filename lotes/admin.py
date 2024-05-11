from django.contrib import admin
from .models import Lot, ProductionLine, Product, Distribution, Lot_RawMaterial, Flavor, RawMaterial

# Register your models here.
admin.site.register(Product)
admin.site.register(Lot)
admin.site.register(ProductionLine)
admin.site.register(Distribution)
admin.site.register(Lot_RawMaterial)
admin.site.register(Flavor)
admin.site.register(RawMaterial)