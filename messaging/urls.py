from django.urls import path
from . import views

urlpatterns = [
    path('', views.message_list, name='messages'),
    path('message_detail/<int:pk>', views.message_detail, name='message_detail'),
]