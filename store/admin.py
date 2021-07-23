from django.contrib import admin
from store.models.product import Products
from store.models.category import Category
from store.models.order import Orders
from store.models.customer import CustomerData


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'email']

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


admin.site.register(Products, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(CustomerData, AdminCustomer)
admin.site.register(Orders)
