from django.shortcuts import render, redirect
from store.models.product import Products
from store.models.order import Orders
from store.models.customer import CustomerData
from django.views import View

class CheckOut(View):
    def post(self, request):                                     # it is use for fetch product from products in cart when we click on add to cart
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        user = request.session.get('customer')
        cart = request.session.get('cart')
        products = Products.get_products_by_id(list(cart.keys()))
        print(user, address, phone, cart, products)

        for product in products:
            order = Orders(user = CustomerData(id = user),
                           address= address,
                           phone= phone,
                           product = product,
                           quantity = cart.get(str(product.id)),
                           price = product.price)

            request.session['cart']  = {}              # it is use for clear cart session and create empty cart
        print(request.session.get('customer'))
        return redirect('cart')