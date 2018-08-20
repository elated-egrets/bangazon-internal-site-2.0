from django.contrib.auth.models import User
from django import forms

from website.models import Profile

class ProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Profile
        fields = ('address', 'phone')