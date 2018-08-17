from website.forms import UserForm, ProductForm
from django.shortcuts import render

from website.models import Product


def list_products(request):
    print(request.GET.get('search_terms', ''))
    all_products = Product.objects.all()
    template_name = 'product/list.html'
    return render(request, template_name, {'products': all_products})