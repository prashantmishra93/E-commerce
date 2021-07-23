from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    @staticmethod
    def get_all_category():
        return Category.objects.all()

    def __str__(self):             #it is use to overrite on admin or website page for category ForegionKey
        return self.name