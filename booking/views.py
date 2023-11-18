from django.shortcuts import render, redirect
from .models import BookingDate, Booking, TimeSlot
# Create your views here.


def view_all(request):
    return render(request, 'booking/view_all.html')


def create_booking(request):
    if request.method == 'POST':
        timeslot_id = request.POST.get('booking_slot')
        timeslot = TimeSlot.objects.get(id=timeslot_id)
        Booking.objects.create(timeslot=timeslot)
        return redirect('success_page')  # we need to make a success page

    dates = BookingDate.objects.all().prefetch_related('time_slots')
    return render(request, 'booking/create.html', {'dates': dates})
