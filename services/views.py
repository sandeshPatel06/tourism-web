from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from tourism_app.models import Service, Booking
from tourism_app.forms import BookingForm

def services_list(request):
    """View to list all services."""
    services = Service.objects.all()
    return render(request, 'services/services_list.html', {'services': services})

@login_required
def flight_booking(request):
    """View for flight booking service."""
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid() and form.cleaned_data['service_type'] == 'flight':
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, 'Your flight booking has been submitted successfully!')
            return redirect('booking_success')
    else:
        form = BookingForm(initial={'service_type': 'flight'})
    return render(request, 'services/flight_booking.html', {'form': form})

def hotel_booking(request):
    """View for hotel booking service."""
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid() and form.cleaned_data['service_type'] == 'hotel':
            booking = form.save(commit=False)
            if request.user.is_authenticated:
                booking.user = request.user
            booking.save()
            messages.success(request, 'Your hotel booking has been submitted successfully!')
            return redirect('booking_success')
    else:
        form = BookingForm(initial={'service_type': 'hotel'})
    
    return render(request, 'services/hotel_booking.html', {'form': form})

def car_rental(request):
    """View for car rental service."""
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid() and form.cleaned_data['service_type'] == 'car':
            booking = form.save(commit=False)
            if request.user.is_authenticated:
                booking.user = request.user
            booking.save()
            messages.success(request, 'Your car rental booking has been submitted successfully!')
            return redirect('booking_success')
    else:
        form = BookingForm(initial={'service_type': 'car'})
    
    return render(request, 'services/car_rental.html', {'form': form})