from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponseRedirect
from datetime import datetime, timedelta
from .models import Appointment
from django.contrib import messages

def AppointmentList(request):
    """
    Simply displays all appointments
    """
    appointments = Appointment.objects.all()
    
    return render(
        request,
        "booking/booking.html",
        {"appointments": appointments,
        },
    )