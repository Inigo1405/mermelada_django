from django.contrib import admin
from .models import RawMaterials, QualityReport, RawMaterialsLote, Distribution 

# Register your models here.
admin.site.register(RawMaterials)
admin.site.register(QualityReport)
admin.site.register(RawMaterialsLote)
admin.site.register(Distribution)

