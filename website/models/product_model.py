from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
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
    image = models.ImageField(upload_to='', height_field=None, width_field=None, max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=1)
    local_delivery = models.BooleanField()

    def __str__(self):
        return self.title
