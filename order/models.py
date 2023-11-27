from django.db import models
from products.models import Products
from customers.models import Customer

# Create your models here.
class Order(models.Model):
    product_id = models.ManyToManyField(Products)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return f'{Customer.pk}-{Products.pk}-{self.quantity}'