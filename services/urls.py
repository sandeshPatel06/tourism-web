from django.urls import path
from . import views

urlpatterns = [
    path('', views.services_list, name='services_list'),
    path('flight-booking/', views.flight_booking, name='flight_booking'),
    path('hotel-booking/', views.hotel_booking, name='hotel_booking'),
    path('car-rental/', views.car_rental, name='car_rental'),
]