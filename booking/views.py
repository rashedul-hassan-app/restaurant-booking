from django.shortcuts import render, redirect
from .models import BookingDate, Booking, TimeSlot
from .forms import TimeSlotForm
from django.contrib import messages
from datetime import date, timedelta
# Create your views here.


def view_all(request):
    return render(request, 'booking/view_all.html')


def create_booking(request):
    if request.method == 'POST':
        timeslot_id = request.POST.get('booking_slot')
        timeslot = TimeSlot.objects.get(id=timeslot_id)
        Booking.objects.create(timeslot=timeslot)
        messages.success(request, 'Booking created successfully!')
        return redirect('booking_page')

    dates = BookingDate.objects.all().prefetch_related('time_slots')
    return render(request, 'booking/create.html', {'dates': dates})


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
