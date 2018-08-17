from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class PaymentType(models.Model):
    """This model represent payment types available to a user

    Written By: Katheryn Ford
    """

    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    name = models.CharField(max_length=255)
    cc_number  = models.PositiveSmallIntegerField()
    cvv = models.PositiveSmallIntegerField()
    expiration_date = models.DateField()