from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('production/', views.production, name='production_status'),
    path('production_update/', views.production_update, name='production_update'),
    path('flavors/', views.flavor_crud, name='flavor_crud'),
    path('flavors/<int:id>/', views.flavor_crud, name='flavor_crud_id'),
    path('lots/', views.lot, name='lots'),
    path('raw_materials/', views.rawMaterial, name='rawMaterial'),
    path('distributions/', views.distribution, name='distribution'),
    path('products/', views.manage_products, name='manage_products'),
    path('login/', views.login_view, name='login'),
    path('production/', views.view_production, name='view_production'),
    path('customer/products_flavors/', views.view_products_and_flavors, name='view_products_and_flavors'),
    path('logout/', views.logout_view, name='logout'),
    path('manager_dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('customer_dashboard/', views.customer_dashboard, name='customer_dashboard'),
    path('signup/', views.signup, name='signup'),
    path('create/', views.tu_vista, name='xd'),
    path('profile/', views.profile, name='profile'),
    path('changeUser', views.edit_user, name='change_user'),
    path('<int:id>/password/', views.change_password, name='change_password'),
    path('users/', views.users, name='users'),
]
