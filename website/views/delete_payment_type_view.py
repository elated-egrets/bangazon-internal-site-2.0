from website.forms import UserForm, PaymentTypeForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from website.models import PaymentType

@login_required
def delete_payment_type(request, payment):


    all_payment_types = PaymentType.objects.all()
    print(all_payment_types)
    current_payment_type= next((item for item in all_payment_types if str(item.id) == str(payment)), None)


    template_name = 'payment_type/delete.html'
    if current_payment_type != None:
        query = PaymentType.objects.get(pk=payment)
        query.delete()
        return render(request, template_name, {})
    else:
        return render(request, 'website/404.html', {})
