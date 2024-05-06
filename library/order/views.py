from django.shortcuts import render, redirect

from authentication.views import librarian_required
from .models import Order
from book.models import Book

from order.forms import *

@librarian_required
def orders(request):
    us1 = request.user.role
    if us1 == 1:
        all_orders1 = Order.get_all()
        context = {'all_orders': all_orders1, 'role': us1, 'active_page': 'orders'}
        return render(request, 'order/all_orders.html', context)
    else:
        return redirect('/order/my_orders')

def all_user_orders(request):
    us1 = request.user.role
    if us1 == 0:
        all_orders2 = Order.objects.filter(user=request.user)
        context = {'all_user_orders': all_orders2, 'role': us1, 'active_page': 'orders'}
        return render(request, 'order/all_user_orders.html', context)
    else:
        return redirect('/books')

def create_order(request):
    us1 = request.user.role
    if us1 == 0:
        if request.method == "POST":
            form = OrderForm(request.POST)
            if form.is_valid():
                order = form.save(commit=False)
                order.user_id = request.user.id
                form.save()
                return redirect('all_user_orders')
            else:
                error_message = "Failed to create order. Check if the book is already ordered or if the book count is 1."
                return render(request, 'order/create_order.html', {'form': form, 'error_message': error_message})
        else:
            form = OrderForm()
            return render(request, 'order/create_order.html', {'form': form})
    else:
        return redirect('orders')
def delete_order(request, order_id):
    Order.delete_by_id(order_id)
    return redirect('/orders')