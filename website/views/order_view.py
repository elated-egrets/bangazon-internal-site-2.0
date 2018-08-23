from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from website.models import Order
from website.models import Product
from website.views import index_view
import json

@login_required
def order_view(request):
    """View to all the user to delete an order

    Arguments:


    Written By:
    """

    current_user = request.user
    users_orders = current_user.order_set.all()

    # try to find one that has not yet been closed
    open_order = next((order for order in users_orders if order.date_closed == None), None)

    if request.method == "GET":
        return render(request, 'website/order.html', {"order": open_order})
    elif request.method == "POST":
        # check for what type of post it was
        if "delete_order" in request.POST:
            # if it was a delete order post, delete the order and send the user back to the index
            open_order.delete()
            return redirect('/')
        elif "delete_product" in request.POST:
            # if it was a delete product post, get the product and remove it from the order
            # get product reference
            product_to_remove = Product.objects.get(pk=request.POST.get('delete_product'))
            # remove that product from the order
            open_order.products.remove(product_to_remove)
            # return the same object as the get request
            return render(request, 'website/order.html', {"order": open_order})

