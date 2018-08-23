"""  
    module: order history detail view
    author: riley mathews
    purpose: to create an order detail view
"""
from website.models import Order
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def order_history_detail_view(request, order):
    """ function to create a detail view for a past order """
    current_order = Order.objects.get(pk=order)
    print(current_order)
    products = current_order.products.all()
    order_total = sum([product.price for product in products])
    print(products)
    return render(request, 'website/order_history_detail.html', {'order_products': products, 'order_total': order_total})