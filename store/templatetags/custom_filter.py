from django import template

register = template.Library()


@register.filter(name="currency")           # it's filter use for get currency symbol in page
def currency(number):
    return "₹ " + str(number)

@register.filter(name="multiply")
def multiply(number, number1):
    return number * number1