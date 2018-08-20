from django.db import models
from .payment_types_model import PaymentType
from django.contrib.auth.models import User
from .product_model import Product

"""  
    module: order model
    author: riley mathews
    purpose: to creat the data model for an order
"""


class Order(models.Model):
    products = models.ManyToManyField(Product)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE, blank=True, null=True)
    date_created = models.DateField()
    date_closed = models.DateField(blank=True, null=True)