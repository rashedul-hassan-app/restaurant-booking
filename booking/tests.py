from .forms import BookingForm
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import BookingDate, TimeSlot, Booking
from datetime import date, timedelta, time


class BookingFormTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_create_booking(self):
        # Create a booking date
        booking_date = BookingDate.objects.create(date=date.today())
        # Create a time slot for the booking date
        time_slot = TimeSlot.objects.create(
            date=booking_date, time=('10:00'))

        response = self.client.post(reverse('create_booking'), {
            'booking_slot': time_slot.id})
        # Redirects after successful booking
        self.assertEqual(response.status_code, 302)

        # Ensure booking is created
        self.assertTrue(Booking.objects.filter(
            user=self.user, timeslot=time_slot).exists())

    def test_add_timeslot(self):
        booking_date = BookingDate.objects.create(date=date.today())
        response = self.client.post(reverse('add_timeslot'), {
                                    'time': '14:00', 'date': booking_date.id})
        # Redirects after successful time slot addition
        self.assertEqual(response.status_code, 302)
        # Ensure time slot is added
        self.assertTrue(TimeSlot.objects.filter(
            time=time(hour=14, minute=0), date=booking_date).exists())

    def test_booking_form_date_field_label(self):
        form = BookingForm()
        self.assertTrue(
            form.fields['timeslot'].label is None or form.fields['timeslot'].label == 'timeslot')

    def test_view_all_bookings(self):
        # reverse requires the 'name' in the views file
        response = self.client.get(reverse('booking_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking/view_all.html')

    def test_edit_booking(self):
        # Create a booking
        booking_date = BookingDate.objects.create(date=date.today())
        time_slot = TimeSlot.objects.create(
            date=booking_date, time=time(hour=10, minute=0))
        booking = Booking.objects.create(user=self.user, timeslot=time_slot)

        # Edit the booking
        new_time_slot = TimeSlot.objects.create(
            date=booking_date, time=time(hour=11, minute=0))
        response = self.client.post(reverse('edit_booking', kwargs={
                                    'booking_id': booking.id}), {'timeslot': new_time_slot.id})

        # Redirects after successful edit
        self.assertEqual(response.status_code, 302)
        # Ensure booking is updated
        self.assertEqual(Booking.objects.get(
            id=booking.id).timeslot, new_time_slot)

    def test_delete_booking(self):
        # Create a booking
        booking_date = BookingDate.objects.create(date=date.today())
        time_slot = TimeSlot.objects.create(
            date=booking_date, time=time(hour=10, minute=0))
        booking = Booking.objects.create(user=self.user, timeslot=time_slot)

        # Delete the booking
        response = self.client.post(
            reverse('delete_booking', kwargs={'booking_id': booking.id}))

        # Redirects after successful deletion
        self.assertEqual(response.status_code, 302)
        # Ensure booking is deleted
        self.assertFalse(Booking.objects.filter(id=booking.id).exists())
