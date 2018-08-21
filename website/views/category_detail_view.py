from django.shortcuts import render

from website.models import Category, Product

def category_detail_view(request, category):
    '''View for category detail page

        Author: Levi Schubert

        allowed verbs: GET

        returns render of template with category and links to all products from the category
    '''

    if request.method == 'GET':
        category_detail = Category.objects.get(pk=category)
        products = Product.objects.filter(category=category)
        num_of_listings = len(products)
        template_name = 'website/category_detail.html'
        return render(request, template_name, {'category': category_detail, 'products': products, 'listings': num_of_listings})