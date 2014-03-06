from django.contrib.auth.models import User
from django.db import models
from checkout.models import Customer
from storefront.models import Product


class Review(models.Model):
    comment = models.TextField()
    product = models.ForeignKey(Product)
    customer = models.ForeignKey(Customer)