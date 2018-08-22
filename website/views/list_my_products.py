from website.forms import UserForm, ProductForm
from django.shortcuts import render
from collections import Counter

from website.models import Product, Order
from django.contrib.auth.decorators import login_required


@login_required
def list_my_products(request):
    """View for listing a user's products for sale
    
    Arguments:
        request {http get} -- http request that triggered function
    
    Returns:
        render -- renders the list of user's products via html template

    Written By: Katheryn Ford
    """
    # get all orders
    # create an empty dict, keys will be product ids, and value will be how many have sold
    product_counter = Counter([product for order in Order.objects.all() for product in order.products.all()])
    # loop through orders and loop through products, for each one add one to the value of the id on the dict
    print(product_counter)
    current_user = request.user
    filtered_products = Product.objects.filter(seller_id=current_user)
    product_info = list()
    for product in filtered_products:
        if product_counter[product]:
            product_info.append({'product': product, 'number_sold': product_counter[product], 'number_remaining': product.quantity - product_counter[product]})
            print(product_info)
    template_name = 'product/my_products.html'
    return render(request, template_name, {'products': product_info})