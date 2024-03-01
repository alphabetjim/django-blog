from django.shortcuts import render, get_object_or_404
from .models import Message

def message_list(request):
    messages = Message.objects.all()
    return render(request, 'messaging/message_list.html', {'messages': messages})

def message_detail(request, pk):
    message = get_object_or_404(Message, pk=pk)
    return render(request, 'messaging/message_detail.html', {'message': message})