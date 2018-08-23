from django.shortcuts import render, redirect
from website.models import PaymentType
import datetime
from django.contrib.auth.decorators import login_required

"""  
    module: complete order view
    author: riley mathews
    purpose: for the user to come to add a payment type to their order and complete it
"""

@login_required
def complete_order_view(request):
    """ function to generate view for completing an order """
    print(request.POST.get('payment'))
    current_user = request.user

    if request.method == "GET":
        payment_types = current_user.paymenttype_set.all()
        return render(request, 'website/complete_order.html', {'payment_types': payment_types})
    elif request.method == "POST":
        # get the open order
        open_order = next((order for order in current_user.order_set.all() if order.date_closed == None), None)
        # get the payment based on id from the form
        payment_selected = PaymentType.objects.get(pk=request.POST.get('payment'))
        # set the order payment and date closed
        open_order.payment_type = payment_selected
        open_order.date_closed = datetime.datetime.now()
        # save the order
        open_order.save()
        # redirect the user back to their cart
        return redirect('/cart')