from website.forms import UserForm, PaymentTypeForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from website.models import Product

@login_required
def delete_my_product(request, product):
    """View to all the user to delete a payment type
    
    Arguments:
        request {[http get]} -- [The automatically generated request object]
        payment {[int]} -- [Primary Key of the payment type to be deleted]

    Written By: Katheryn Ford
    """

    current_product = Product.objects.get(pk=product)


    template_name = 'product/delete.html'
    if current_product != None:
        query = Product.objects.get(pk=product)
        query.delete()
        return render(request, template_name, {})
    else:
        return render(request, 'website/404.html', {})
