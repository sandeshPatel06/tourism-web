from django.urls import path
from . import views
from django.contrib import admin
from accounts.views import logout_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', logout_view, name='logout'),
    path('', views.index, name='index'),
    path('destinations/', views.destinations_view, name='destinations'),
    path('booking/', views.booking_view, name='booking'),
    path('booking/success/', views.booking_success, name='booking_success'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('testimonial/', views.testimonial_view, name='testimonial'),
    path('service/<int:service_id>/', views.service_detail, name='service_detail'),
    # path('destination/<int:destination_id>/', views.destination_detail, name='destination_detail'),
    path('services/', views.service_view, name='services'),
    path('services/add/', views.service_create, name='service_add'),
    
]