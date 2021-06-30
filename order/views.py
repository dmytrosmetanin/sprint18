from django.shortcuts import render, redirect

from .models import Order
from .order_form import OrderForm

from rest_framework import viewsets, filters
from .serializer import *

class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class IsOwnerFilterBackend(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        return queryset.filter(owner=request.user)

class Order_byUserIDView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = Order_by_UserIDSerializer

    filter_backends = [filters.SearchFilter, IsOwnerFilterBackend]
    search_fields = ['first_name']

def order_list(request):
    context = {}
    orders = []
    all_order = Order.get_all()
    for order in all_order:
        order_txt ={'id': order.id,
                    'name': f"{order.user.first_name} {order.user.last_name} {order.user.middle_name}",
                    'book': f"{order.book.name}({order.book.description})"
        }
        orders.append(order_txt)

    context.update({'all_order': orders})
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