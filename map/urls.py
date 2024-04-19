from django.urls import path
from . import views

urlpatterns = [
    path('vehicle-positions/', views.vehicle_positions, name='vehicle_positions'),
]
