from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponseRedirect
from datetime import datetime, timedelta
from .models import Appointment
from .forms import BookingForm
from django.contrib import messages
from django.db.models import Q

# functions
# from example
def dayToWeekday(x):
    z = datetime.strptime(x, "%Y-%m-%d")
    y = z.strftime('%A')
    return y


def AppointmentList(request):
    """
    Simply displays all appointments
    """
    if request.user.is_superuser:
        appointments = Appointment.objects.all()
    else:
        appointments = Appointment.objects.all().filter(Q(user_id = request.user.id)).values()
    # for appointment in appointments:
    #     #print(dayToWeekday(appointment['day']))
    #     field_name = 'day'
    #     # field_value = getattr(appointment, field_name)
    #     # print(field_value)
    #     print(appointment)
    #     for field in appointment:
    #         print(field)
    #         if field == 'day':
    #             print(appointment[field])
    #             #print(dayToWeekday(appointment[field]))
    #             #print(appointment[field].strftime('%A'))
    return render(
        request,
        "booking/booking.html",
        {"appointments": appointments,
        },
    )

def booking_form(request):
    """
    Display booking form to instantiate appointment
    """
    print(request.user)
    if request.method == "POST":
        form = BookingForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.user = request.user
            form.save()
            return redirect(AppointmentList)
    else:
        form = BookingForm(user=request.user)
    
    return render(
        request,
        "booking/booking_form.html",
        {
            "booking_form": form,
        }
    )
    