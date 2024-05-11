from django.urls import path
from . import views

urlpatterns = [ #Lista que tiene el registro de todas las direcciones
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
]
   