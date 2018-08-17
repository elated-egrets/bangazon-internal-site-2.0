from django.db import models

class Category(models.model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name