from django.shortcuts import render

from website.models import Category, Product

def category_view(request):
    '''View for category page

        Author: Levi Schubert

        allowed verbs: GET

        returns render of template with categories and links to the first three products from each
    '''

    if request.method == 'GET':
        categories = Category.objects.all()
        data_set = []
        for category in categories:
            data_set.insert(len(data_set), (category, Product.objects.filter(category=category)[:3]))
        
        template_name = 'website/category.html'
        return render(request, template_name, {'data_set': data_set})