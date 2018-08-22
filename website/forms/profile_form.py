from django.contrib.auth.models import User
from django import forms

from website.models import Profile

'''Form for user fields as well as the address and phone fields for profile'''
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('address', 'phone')