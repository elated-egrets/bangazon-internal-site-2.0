from website.forms import UserForm, ProductForm

from website.models import Product


def list_products(request):
    all_products = Product.objects.all()
    template_name = 'product/list.html'
    return render(request, template_name, {'products': all_products})