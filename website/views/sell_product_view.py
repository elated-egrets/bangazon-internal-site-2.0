from website.forms import UserForm, ProductForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from website.models import Product, Category



@login_required
def sell_product(request):
    if request.method == 'GET':
        product_form = ProductForm()
        template_name = 'product/create.html'
        return render(request, template_name, {'product_form': product_form})

    elif request.method == 'POST':
        data = Product(
            seller = request.user,
            title = request.POST['title'],
            description = request.POST['description'],
            price = request.POST['price'],
            quantity = request.POST['quantity'],
            category = Category.objects.get(id=request.POST['category'])
        )
        form = ProductForm(data=request.POST, files=request.FILES, instance= data)
        form.save()

        # request.POST['seller'] = request.user
        # all_data = request.POST.copy()
        # all_data['seller_id'] = request.user
        # form_data = ProductForm(request.POST, request.FILES)
        # form_data.data['seller'] = request.userz
        
        # form_data.save()

        # file_data = {'image': SimpleUploadedFile(request.FILES['image'], <file data>)}
        # p = ContactFormWithMugshot(data, file_data)

        # p.save()
        return HttpResponseRedirect(f'/products/{data.id}')