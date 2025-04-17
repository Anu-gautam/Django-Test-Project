from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Order
from menu.models import FoodItem

@login_required
def dashboard(request):
    orders = Order.objects.filter(user=request.user)
    total_orders = orders.count()
    total_spent = sum(order.total for order in orders)

    return render(request, 'orders/dashboard.html', {
        'orders': orders,
        'total_orders': total_orders,
        'total_spent': total_spent
    })
