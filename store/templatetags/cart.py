from django import template

register = template.Library()


@register.filter(name="is_in_cart")
def is_in_cart(product, cart):                          # it is use for check product in cart through key
    keys = cart.keys()
    for id in cart:
        if int(id) == product.id:
            return True
    return False


@register.filter(name="cart_quantity")
def cart_quantity(product, cart):              # it is use for get product quantity in cart
    keys = cart.keys()
    for id in cart:
        if int(id) == product.id:
            return cart.get(id)
    return 0

@register.filter(name="price_total")
def price_total(product, cart):                            # it is use for get total price of no. of products
    total = product.price * cart_quantity(product, cart)
    return total

@register.filter(name="total_cart_price")          # it is use for get sum of all cart product price
def total_cart_price(products, cart):
    sum = 0;
    for p in products:
        sum += price_total(p , cart)

    return sum