from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    """
    Form class for users to write a message on post 
    """
    class Meta:
        model = Message
        fields = ('receiver','subject','body',)
