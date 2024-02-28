from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponseRedirect
from datetime import datetime, timedelta
from .models import Appointment
from django.contrib import messages
from django.db.models import Q

def AppointmentList(request):
    """
    Simply displays all appointments
    """
    if request.user.is_superuser:
        appointments = Appointment.objects.all()
    else:
        appointments = Appointment.objects.all().filter(Q(user_id = request.user.id)).values()
    print(len(appointments))
    print(request.user.id)
    return render(
        request,
        "booking/booking.html",
        {"appointments": appointments,
        },
    )

# def Appointment_page(request):
#     """
#     Returns 
#     """