from django import forms
from .models import Appointment


class BookingForm(forms.ModelForm):
    """
    Form class for users to request a collaboration 
    """
    class Meta:
        model = Appointment
        fields = ('day', 'time',)

    def __init__(self, **kwargs):
        self.user = kwargs.pop('user')
        print(self.user)
        super(BookingForm, self).__init__(**kwargs)

    def save(self, commit=True):
       appointment = super(BookingForm, self).save(commit=False)
       appointment.user = self.user
       if commit:
           appointment.save()
       return appointment