""" 
    module: product detail view
    author: riley mathews
    purpose: to create a function based view that will show the details of a single product
"""
from django.http import HttpResponse
from website.models import Product
from django.shortcuts import render

def product_detail(request, product):
    """function to make the view for a product detail
    
    Arguments:
        request {http} -- the request that triggered the function
        product {string} -- passed into the function from the url, expected to be the id of the product we are looking for
    
    Returns:
        render -- function either renders the product detail html page, or an error page if the product was not found
    """
    # get all of the products
    all_products = Product.objects.all()
    # find the product who's id is equal to the one passed to the function
    # currently the product is coming from the url
    current_product = next((item for item in all_products if int(item.id)==int(product)), None)

    for key, value in current_product.__dict__.items():
        print(key, value)

    # define the template to be used
    template_name = 'website/product_detail.html'
    if current_product != None:
        return render(request, template_name, {'product': current_product})
    else:
        return render(request, 'website/404.html', {})

