"""  
    module: order history view
    author: riley mathews
    purpose: to generate a view for the current users order history
"""

from website.models import Order
from django.shortcuts import render

def order_history_view(request):
    """ function for creating the order history view """
    current_user = request.user
    order_history = [order for order in current_user.order_set.all() if order.date_closed != None]
    return render(request, 'website/order_history.html', {'order_history': order_history})