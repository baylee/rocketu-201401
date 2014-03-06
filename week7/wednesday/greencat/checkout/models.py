from django.contrib.auth.models import User
from django.db import models
from storefront.models import Product


class Customer(User):
    num_of_cats = models.PositiveIntegerField()


class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer)
    products = models.ManyToManyField(Product)