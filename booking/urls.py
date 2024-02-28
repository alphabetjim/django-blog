from django.urls import path
from . import views

urlpatterns = [
    path('', views.AppointmentList, name='booking'),
    path('booking_form', views.booking_form, name='booking_form'),
]