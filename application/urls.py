from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show_services/', views.show_services, name='show_services'),
    path('show_orders/', views.show_orders, name='show_orders'),
    path('add_vehicle_model/', views.add_vehicle_model, name='add_vehicle_model'),
    path('add_vehicle/', views.add_vehicle, name='add_vehicle'),
]
