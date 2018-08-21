from django.shortcuts import render

"""  
    module: complete order view
    author: riley mathews
    purpose: for the user to come to add a payment type to their order and complete it
"""

def complete_order_view(request):
    """ function to generate view for completing an order """
    return render(request, 'website/complete_order.html', {})