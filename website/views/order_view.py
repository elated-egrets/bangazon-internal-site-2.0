from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from website.models import Order

@login_required
def order_view(request):
    """View to all the user to delete an order

    Arguments:


    Written By:
    """

    current_user = request.user
    users_orders = current_user.order_set.all()

    # try to find one that has not yet been closed
    open_order = next((order for order in users_orders if order.date_closed == None), None)

    if request.method == "GET":
        return render(request, 'website/order.html', {"order": open_order})
    elif request.method == "POST":
        open_order.delete()
        return render(request, 'index.html', {})


    # template_name = 'order/delete.html'
    # if current_order != None:
    #     query = OrderType.objects.get(pk=order)
    #     query.delete()
    #     return render(request, template_name, {})
    # else:
    #     return render(request, 'website/404.html', {})




    # all_payment_types = PaymentType.objects.all()
    # print(all_payment_types)
    # current_payment_type= next((item for item in all_payment_types if str(item.id) == str(payment)), None)


    # template_name = 'payment_type/delete.html'
    # if current_payment_type != None:
    #     query = PaymentType.objects.get(pk=payment)
    #     query.delete()
    #     return render(request, template_name, {})
    # else:
    #     return render(request, 'website/404.html', {})