from website.forms import UserForm, ProductForm
from django.shortcuts import render
from website.models import Product


def list_products(request):
    """function to define the view of listing products
    
    Arguments:
        request {http get} -- http request that triggered function
    
    Returns:
        render -- renders the list of products via html template
    """
    search_terms = request.GET.get('search_terms', '')
    local_search = request.GET.get('local_search', '')
    all_products = Product.objects.all()
    if search_terms != '':
        all_products = [item for item in all_products if search_terms in item.title]
    if local_search != '':
        all_products = [item for item in all_products if search_terms in item.seller.profile.city and item.local_delivery == True]
    template_name = 'product/list.html'
    return render(request, template_name, {'products': all_products})