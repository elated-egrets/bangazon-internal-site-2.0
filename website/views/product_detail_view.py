""" 
    module: product detail view
    author: riley mathews
    purpose: to create a function based view that will show the details of a single product
"""
from django.http import HttpResponse
from website.models import Product, Order
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
import datetime

def product_detail(request, product):
    """function to make the view for a product detail
    
    Arguments:
        request {http} -- the request that triggered the function
        product {string} -- passed into the function from the url, expected to be the id of the product we are looking for
    
    Returns:
        render -- function either renders the product detail html page, or an error page if the product was not found
    """
    # try to get product object
    try:
        current_product = Product.objects.get(pk=product)
    except ObjectDoesNotExist:
        return render(request, 'website/404.html', {})

    if request.method == "GET":
        # define template name for get requests
        template_name = 'website/product_detail.html'

        # get how many of this product is remaining
        product_remaining = current_product.quantity - len([product for order in Order.objects.all()  for product in order.products.all() if product.id==current_product.id])
        print(product_remaining)
        # finally render product template
        return render(request, template_name, {'product': current_product, 'remaining': product_remaining})

    elif request.method == "POST":
    # get user
        current_user = request.user
        # get or create a user order 
        
        current_order = current_user.order_set.all().filter(date_closed!=None)
    
        current_order.save()
        
        # add product 
        current_order.products.add(current_product)

        return render(request, 'website/product_add_sucsess.html', {'product': current_product})
