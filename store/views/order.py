from django.shortcuts import render, redirect
from store.models.product import Products
from django.views import View
from store.models.order import Orders

class OrderView(View):

    def get(self, request):                                     # it is use for fetch product from products in cart when we click on add to cart
        customer = request.session.get('customer')
        order = Orders.get_order_by_user(customer)
        print(order)
        return render(request, 'order.html', {'order':order})
