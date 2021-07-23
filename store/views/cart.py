from django.shortcuts import render, redirect
from store.models.product import Products
from django.views import View

class Cart(View):
    def get(self, request):                                     # it is use for fetch product from products in cart when we click on add to cart
        ids = list(request.session.get('cart').keys())
        products = Products.get_products_by_id(ids)
        print(ids, products)
        return render(request, 'cart.html', {'products':products})
