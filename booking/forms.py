from django import forms
from .models import TimeSlot


class TimeSlotForm(forms.ModelForm):
    class Meta:
        model = TimeSlot
        fields = ['time', 'date']
        widgets = {
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'date': forms.Select()
        }
