from django.db import models
from .category import Category

class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=0)
    description = models.CharField(max_length=100, default='', null=True, blank=True)
    image = models.ImageField(upload_to='products/')

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter(id__in = ids)     #it is pass a list

    @staticmethod
    def get_all_products():
        return Products.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):             # this function will be create for get data by id from database
        if category_id:
            return Products.objects.filter(category = category_id)     # if we pass category id then the show of that category product
        else:
            return Products.get_all_products()             # otherwise show all product