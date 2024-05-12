from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('production/', views.production, name='production_status'),
    path('production_update/', views.production_update, name='production_update'),
    path('flavors/<int:id>/', views.flavor_crud, name='flavor_crud_id'),
    path('flavors/', views.flavor_crud, name='flavor_crud'),
    path('products/', views.manage_products, name='manage_products'),
    path('login/', views.login_view, name='login'),
    path('customer/production/', views.view_production, name='view_production'),
    path('customer/products_flavors/', views.view_products_and_flavors, name='view_products_and_flavors'),
    path('logout/', views.logout_view, name='logout'),
    path('manager_dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('customer_dashboard/', views.customer_dashboard, name='customer_dashboard'),
    path('signup/', views.signup, name='signup'),
]
