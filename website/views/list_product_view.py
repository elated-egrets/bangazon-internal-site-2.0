from website.forms import UserForm, ProductForm
from django.shortcuts import render

from website.models import Product


def list_products(request):
    search_terms = request.GET.get('search_terms', '')
    all_products = Product.objects.all()
    if search_terms != '':
        all_products = [item for item in all_products if search_terms in item.title]
    template_name = 'product/list.html'
    return render(request, template_name, {'products': all_products})