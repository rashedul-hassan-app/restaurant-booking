from django.shortcuts import get_object_or_404, render, redirect
from .models import BookingDate, Booking, TimeSlot
from .forms import TimeSlotForm, BookingForm
from django.contrib import messages
from datetime import date, timedelta
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def view_all(request):
    user_bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking/view_all.html', {'bookings': user_bookings})


def create_booking(request):
    if request.method == 'POST':
        timeslot_id = request.POST.get('booking_slot')
        timeslot = TimeSlot.objects.get(id=timeslot_id)
        Booking.objects.create(user=request.user, timeslot=timeslot)
        messages.success(request, 'Booking created successfully!')
        return redirect('booking_page')

    dates = BookingDate.objects.all().prefetch_related('time_slots')
    return render(request, 'booking/create.html', {'dates': dates})


def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)

        if form.is_valid():
            form.save()
            messages.success(request, 'Booking updated successfully!')
            return redirect('booking_page')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'booking/edit_booking.html', {'form': form, 'booking_id': booking_id})


def delete_booking(request, booking_id):
    pass


def add_timeslot(request):
    for i in range(7):
        day = date.today() + timedelta(days=i)
        BookingDate.objects.get_or_create(date=day)

    if request.method == 'POST':
        form = TimeSlotForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Time slot added successfully!')
            return redirect('booking_page')
    else:
        form = TimeSlotForm()

    return render(request, 'booking/add_timeslot.html', {'form': form})
