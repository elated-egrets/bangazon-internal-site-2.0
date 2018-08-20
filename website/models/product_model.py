from django.contrib.auth.models import User
from django.db import models
from .category_model import Category

# Create your models here.
class Product(models.Model):
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=1)