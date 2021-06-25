from django.shortcuts import render, redirect

from .models import Order
from .order_form import OrderForm
# Create your views here.

def order_list(request):
    context = {}
    all_order = Order.get_all()
    context.update({'all_book': all_order})
    return render(request, 'order/all_order.html', context)


def order_form(request, id = 0):
    if request.method == 'GET':
        if id == 0:
            form = OrderForm()
        else:
            order = Order.get_by_id(id)
            form = OrderForm(instance=order)

        return render(request, 'order/order_form.html', {'form': form})
    else:
        if id == 0:
            form = OrderForm(request.POST)

        else:
            order = Order.get_by_id(id)
            form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
        return redirect('order:order_list')

def order_delete(request, id):
    Order.delete_by_id(id)
    return redirect('order:order_list')