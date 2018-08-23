from website.forms import UserForm, PaymentTypeForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from website.models import PaymentType


@login_required
def add_payment_type(request):
    """View for adding a payment type
    
    Written by: Katheryn Ford
    """

    if request.method == 'GET':
        payment_type_form = PaymentTypeForm()
        template_name = 'payment_type/add.html'
        return render(request, template_name, {'payment_type_form': payment_type_form})

    elif request.method == 'POST':
        form_data = request.POST

        pt = PaymentType(
            user = request.user,
            name = form_data['name'],
            cc_number = form_data['cc_number'],
            cvv = form_data['cvv'],
            expiration_date = form_data['expiration_date'],
        )
        pt.save()
        template_name = 'profile/profile.html'
        return render(request, template_name, {})