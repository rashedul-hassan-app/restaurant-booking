from django import forms
from .models import TimeSlot, Booking
from django.db.models import Q


class TimeSlotForm(forms.ModelForm):
    class Meta:
        model = TimeSlot
        fields = ['time', 'date']
        widgets = {
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'date': forms.Select()
        }


class BookingForm(forms.ModelForm):
    timeslot = forms.ModelChoiceField(queryset=TimeSlot.objects.none())

    class Meta:
        model = Booking
        fields = ['timeslot']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(BookingForm, self).__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            # if editing an existing booking, include the timeslot
            self.fields['timeslot'].queryset = TimeSlot.objects.filter(
                Q(booking__isnull=True) | Q(
                    id=self.instance.timeslot.id)
            )
        else:
            self.fields['timeslot'].queryset = TimeSlot.objects.filter(
                booking__isnull=True)
