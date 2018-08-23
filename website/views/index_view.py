from django.shortcuts import render
from django.template import RequestContext
from website.models import Product



def index(request):
    template_name = 'index.html'
    products = Product.objects.all().order_by('-id')[:20]
    return render(request, template_name, {'products': products})