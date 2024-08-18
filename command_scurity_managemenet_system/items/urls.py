from django.urls import path
from . import views

# urlpatterns = [
#     path('devices/', views.devices_list, name='devices_list'),
#     path('devices/<int:pk>/', views.devices_detail, name='devices_detail'),
#     path('devices/new/', views.devices_create, name='devices_create'),
#     path('devices/<int:pk>/edit/', views.devices_update, name='devices_update'),
#     path('devices/<int:pk>/delete/', views.devices_delete, name='devices_delete'),
#     # outras URLs
# ]
urlpatterns = [
#list
    path('devices/', views.devices_list, name='devices_list'),
    path('equipments/', views.equipments_list, name='equipments_list'),
    path('vehicles/', views.vehicles_list, name='vehicles_list'),
#detail
    path('devices/<int:pk>/', views.devices_detail, name='devices_detail'),
    path('equipments/<int:pk>/', views.equipments_detail, name='equipments_detail'),
    path('vehicles/<int:pk>/', views.vehicles_detail, name='vehicles_detail'),
#create
    path('devices/new', views.devices_create, name='devices_create'),
    path('equipments/new', views.equipments_create, name='equipments_create'),
    path('vehicles/new', views.vehicles_create, name='vehicles_create'),

#update
    path('devices/<int:pk>/edit/', views.devices_update, name='devices_update'),
    path('equipments<int:pk>/edit/', views.equipments_update, name='equipments_update'),
    path('vehicles<int:pk>/edit/', views.vehicles_update, name='vehicles_update'),


#delete    
    path('devices/<int:pk>/delete/', views.devices_delete, name='devices_delete'),
    path('equipments/<int:pk>/delete/', views.equipments_delete, name='equipments_delete'),
    path('vehicles/<int:pk>/delete/', views.vehicles_delete, name='vehicles_delete'),
]
