from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Destination, Service, Booking, Testimonial
from .forms import BookingForm, ContactForm, TestimonialForm, ServiceForm

def index(request):
    """View for the homepage."""
    popular_destinations = Destination.objects.filter(popular=True)[:3]
    services = Service.objects.all()[:3]
    testimonials = Testimonial.objects.filter(is_approved=True)[:3]
    
    # Handle contact form submission
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('index')
    else:
        contact_form = ContactForm()
    
    context = {
        'popular_destinations': popular_destinations,
        'services': services,
        'testimonials': testimonials,
        'contact_form': contact_form,
    }
    return render(request, 'tourism_app/index.html', context)

def destinations_view(request):
    """View for destinations page."""
    destinations = Destination.objects.all()
    return render(request, 'tourism_app/destinations.html', {'destinations': destinations})

@login_required
def booking_view(request):
    """View for booking services."""
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, 'Your booking has been submitted successfully!')
            return redirect('booking_success')
    else:
        form = BookingForm()
    
    context = {
        'form': form,
    }
    return render(request, 'tourism_app/booking.html', context)

@login_required
def booking_success(request):
    """View for successful booking."""
    return render(request, 'tourism_app/booking_success.html')

@login_required
def my_bookings(request):
    """View for user's bookings."""
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'tourism_app/my_bookings.html', {'bookings': bookings})

def testimonial_view(request):
    """View for submitting testimonials."""
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your testimonial! It will be reviewed shortly.')
            return redirect('index')
    else:
        form = TestimonialForm()
    
    return render(request, 'tourism_app/testimonial.html', {'form': form})

def service_detail(request, service_id):
    """View for service details."""
    service = get_object_or_404(Service, pk=service_id)
    return render(request, 'tourism_app/service_detail.html', {'service': service})

def destination_detail(request, destination_id):
    """View for destination details."""
    destination = get_object_or_404(Destination, pk=destination_id)
    return render(request, 'tourism_app/destination_detail.html', {'destination': destination})

def service_view(request):
    """View to list all services."""
    services = Service.objects.all()
    return render(request, 'tourism_app/services.html', {'services': services})

@staff_member_required
def service_create(request):
    """Admin view to add a new service."""
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service added successfully!')
            return redirect('services')
    else:
        form = ServiceForm()
    return render(request, 'tourism_app/service_form.html', {'form': form})