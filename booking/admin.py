from django.contrib import admin
from .models import BookingDate, TimeSlot, Booking
# Register your models here.

admin.site.register(BookingDate)
admin.site.register(TimeSlot)
admin.site.register(Booking)
