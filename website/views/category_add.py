from website.forms import CategoryForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from website.models import Category
from django.http import HttpResponseRedirect


def category_add(request):
    '''view for adding categories
    
        on http request GET returns the form
        on http request POST creates the category and redirects to categories view

        author: Levi Schubert
    '''

    if request.method == 'GET':
        category_form = CategoryForm()
        template_name = 'website/category_add.html'
        return render(request, template_name, {'category_form': category_form})

    elif request.method == 'POST':
        form_data = request.POST

        c = Category(
            name = form_data['name'],
        )
        c.save()
        return HttpResponseRedirect(f'/categories')
