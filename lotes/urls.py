from django.urls import path
from . import views

urlpatterns = [ #Lista que tiene el registro de todas las direcciones
    path('', views.home, name='home'),
    path('production/', views.production, name='production_status'),
    path('production_update/', views.production_update, name='production_update'),
    path('flavors/<int:id>/', views.flavor_crud, name='flavor_crud_id'),
    path('flavors/', views.flavor_crud, name='flavor_crud'),
    path('login/', views.login, name='login'),
    path('products/', views.list_products, name='products'),
    path('lots/', views.lot, name='lots'),
    path('raw_materials/', views.rawMaterial, name='rawMaterial'),
    path('distributions/', views.distribution, name='distribution'),
]
   
