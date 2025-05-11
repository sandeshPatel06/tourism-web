from django.db import models
from django.contrib.auth.models import User

class Destination(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='destinations/')
    location = models.CharField(max_length=100)
    popular = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class Service(models.Model):
    SERVICE_CHOICES = [
        ('flight', 'Flight Booking'),
        ('hotel', 'Hotel Booking'),
        ('car', 'Car Rentals'),
    ]
    
    service_type = models.CharField(max_length=10, choices=SERVICE_CHOICES)
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=50, help_text="Font Awesome class name")
    url = models.URLField(blank=True, null=True, help_text="External URL for service if applicable")
    
    def __str__(self):
        return f"{self.get_service_type_display()} - {self.name}"

class Booking(models.Model):
    SERVICE_CHOICES = [
        ('flight', 'Flight Booking'),
        ('hotel', 'Hotel Booking'),
        ('car', 'Car Rentals'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    service_type = models.CharField(max_length=10, choices=SERVICE_CHOICES)
    destination = models.CharField(max_length=100)
    date = models.DateField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending', 
                              choices=[('pending', 'Pending'), 
                                      ('confirmed', 'Confirmed'), 
                                      ('cancelled', 'Cancelled')])
    
    def __str__(self):
        return f"{self.user.username} - {self.get_service_type_display()} - {self.destination}"

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    image = models.ImageField(upload_to='testimonials/', null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {'Approved' if self.is_approved else 'Pending'}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%Y-%m-%d')}"