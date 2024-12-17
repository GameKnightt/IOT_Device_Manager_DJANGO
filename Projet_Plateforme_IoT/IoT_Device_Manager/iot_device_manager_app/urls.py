from django.urls import path
from django.shortcuts import render
from .views import (
    sensor_list, unit_list, sensor_detail, unit_detail,
    sensor_create, unit_create, sensor_update, unit_update,
    sensor_delete, unit_delete, sensor_visualization
)

def index(request):
    return render(request, 'index.html')

urlpatterns = [
    path('', index, name='index'),
    path('sensors/', sensor_list, name='sensor_list'),
    path('units/', unit_list, name='unit_list'),
    path('sensors/<int:pk>/', sensor_detail, name='sensor_detail'),
    path('units/<int:pk>/', unit_detail, name='unit_detail'),
    path('sensors/add/', sensor_create, name='sensor_create'),
    path('units/add/', unit_create, name='unit_create'),
    path('sensors/<int:pk>/edit/', sensor_update, name='sensor_update'),
    path('units/<int:pk>/edit/', unit_update, name='unit_update'),
    path('sensors/<int:pk>/delete/', sensor_delete, name='sensor_delete'),
    path('units/<int:pk>/delete/', unit_delete, name='unit_delete'),
    path('visualization/', sensor_visualization, name='sensor_visualization'),
    path('visualization/<int:pk>/', sensor_visualization, name='sensor_visualization_detail'),
]