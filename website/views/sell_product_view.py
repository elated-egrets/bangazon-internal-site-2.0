from website.forms import UserForm, ProductForm
from django.shortcuts import render
from django.http import HttpResponseRedirect

from website.models import Product




def sell_product(request):
    if request.method == 'GET':
        product_form = ProductForm()
        template_name = 'product/create.html'
        return render(request, template_name, {'product_form': product_form})

    elif request.method == 'POST':
        form_data = request.POST

        p = Product(
            seller = request.user,
            title = form_data['title'],
            description = form_data['description'],
            price = form_data['price'],
            quantity = form_data['quantity'],
        )
        p.save()
        return HttpResponseRedirect(f'/products/{p.id}')