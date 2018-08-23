"""module: Edit User Form
   author: Jonny Riggs
"""



from django.contrib.auth.models import User
from django import forms

class EditUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('last_name',)