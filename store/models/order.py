from django.db import models
from store.models.customer import CustomerData
from store.models.product import Products
import datetime

class Orders(models.Model):
    user = models.ForeignKey(CustomerData, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=200, default='', blank=True)
    phone = models.CharField(max_length=12, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)


    @staticmethod
    def get_order_by_user(user_id):
        return Orders.objects.filter(user = user_id).order_by('-date')