from website.forms import UserForm, ProductForm
from django.shortcuts import render

from website.models import Product
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
    current_user = request.user
    filtered_products = Product.objects.filter(seller_id=current_user)
    template_name = 'product/my_products.html'
    return render(request, template_name, {'products': filtered_products})