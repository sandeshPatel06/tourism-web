from django.contrib import admin
from .models import Destination, Service, Booking, Testimonial, Contact

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'popular')
    list_filter = ('popular',)
    search_fields = ('name', 'location')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'service_type', 'icon_class')
    list_filter = ('service_type',)
    search_fields = ('name', 'description')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'service_type', 'destination', 'date', 'status', 'created_at')
    list_filter = ('service_type', 'status', 'date')
    search_fields = ('user__username', 'destination', 'email')
    date_hierarchy = 'date'

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_approved', 'created_at')
    list_filter = ('is_approved',)
    search_fields = ('name', 'email', 'message')
    actions = ['approve_selected']

    def approve_selected(self, request, queryset):
        queryset.update(is_approved=True)
    approve_selected.short_description = "Approve selected testimonials"

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_read', 'created_at')
    list_filter = ('is_read',)
    search_fields = ('name', 'email', 'message')
    actions = ['mark_as_read']

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected messages as read"
