from django.contrib import admin
from .models import Lot, Machine, Product, Distribution, Lot_RawMaterial, QualityReport, RawMaterial

# Register your models here.
admin.site.register(Product)
admin.site.register(Lot)
admin.site.register(Machine)
admin.site.register(Distribution)
admin.site.register(Lot_RawMaterial)
admin.site.register(QualityReport)
admin.site.register(RawMaterial)