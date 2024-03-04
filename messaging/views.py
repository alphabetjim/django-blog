from django.shortcuts import render, get_object_or_404
from .models import Message
from .forms import MessageForm

def message_list(request):
    messages = Message.objects.all().filter(receiver = request.user)
    
    if request.method == "POST":
        message_form = MessageForm(data=request.POST)
        if message_form.is_valid():
            message = message_form.save(commit=False)
            message.sender = request.user
            message.save()
    
    message_form = MessageForm()

    return render(request, 
        'messaging/message_list.html',
        {'messages': messages,
            'message_form': message_form,
        },
    )

def message_detail(request, pk):
    message = get_object_or_404(Message, pk=pk)
    return render(request, 'messaging/message_detail.html', {'message': message})