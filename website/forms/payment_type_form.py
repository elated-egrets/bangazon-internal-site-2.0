from django.contrib.auth.models import User
from django import forms

from website.models import PaymentType

class PaymentTypeForm(forms.ModelForm):
    """This form allows a user to add a payment type

    Written by: Katheryn Ford
    """
    class Meta:
        model = PaymentType
        fields = ('name', 'cc_number', 'cvv', 'expiration_date',)