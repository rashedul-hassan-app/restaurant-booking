from django.db import models
from datetime import date, time
from django.conf import settings
# Create your models here.


class BookingDate(models.Model):
    date = models.DateField(unique=True)

    def __str__(self):
        return str(self.date)


class TimeSlot(models.Model):
    time = models.TimeField()
    date = models.ForeignKey(
        BookingDate, related_name='time_slots', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.date.date} at {self.time.strftime('%H:%M')}"


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    timeslot = models.OneToOneField(TimeSlot, on_delete=models.CASCADE)

    def __str__(self):
        return f"Booking for {self.timeslot}"
