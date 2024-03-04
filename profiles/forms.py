from django import forms
from .models import UserProfile


class ProfileForm(forms.ModelForm):
    """
    Form class for users to comment on a post 
    """
    class Meta:
        model = UserProfile
        fields = ('firstname', 'lastname', 'bio',)
