from django.contrib import admin
from django.urls import path, include


urlpatterns = [ #Lista que tiene el registro de todas las direcciones
    path('admin/', admin.site.urls),
    path('',include('lotes.urls')) #Esta es la principal, la del cuetito
]
