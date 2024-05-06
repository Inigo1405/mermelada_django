from django.contrib import admin
from .models import Machine, Product, Lot, RawMaterial, QualityReport, Distribution, Lot_RawMaterial

# Register your models here.
admin.site.register(Machine)
admin.site.register(QualityReport)
admin.site.register(Product)
admin.site.register(Distribution)
admin.site.register(Lot)
admin.site.register(Lot_RawMaterial)
admin.site.register(RawMaterial)

